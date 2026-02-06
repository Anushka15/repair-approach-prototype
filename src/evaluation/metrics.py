from src.database.fetch_data import *
from sqlalchemy import text
import numpy as np
import matplotlib.pyplot as plt
from contextlib import nullcontext
import math

def load_queries_by_blank_lines(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    query_blocks = [q.strip() for q in content.split('\n\n') if q.strip()]
    return query_blocks

from contextlib import nullcontext
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def calculate_expected_values(query_file_name_expected, query_file_name_actual,
                              algorithm_name, engine1, old_table_name, new_table_name,
                              engine2=None, parameters=None):

    is_probabilistic = (algorithm_name == "PRA")

    expected_queries = load_queries_by_blank_lines(query_file_name_expected)
    actual_queries   = load_queries_by_blank_lines(query_file_name_actual)

    if len(expected_queries) != len(actual_queries):
        raise ValueError(f"Mismatch in number of queries: truth={len(expected_queries)}, prob={len(actual_queries)}")

    results = []
    results_with_truth_set = []
    skipped = []  # optional: track skipped query indices + error

    conn2_ctx = engine2.connect() if algorithm_name == "Holo" else nullcontext()

    with engine1.connect() as conn, conn2_ctx as conn2:
        for idx, (expected_q, actual_q) in enumerate(zip(expected_queries, actual_queries), start=1):

            if algorithm_name == "CQA":
                actual_q = actual_q.replace(old_table_name, new_table_name)

            # ---- run expected query (if this fails, you might also want to skip) ----
            try:
                if parameters:
                    expected_result = conn.execute(text(expected_q), parameters).fetchall()
                else:
                    expected_result = conn.execute(text(expected_q)).fetchall()
            except SQLAlchemyError as e:
                conn.rollback()
                skipped.append((idx, "expected_q_failed", str(e)))
                continue

            # ---- run actual query; if it fails, SKIP this query from results ----
            try:
                if parameters:
                    if algorithm_name == "Holo":
                        actual_result = conn2.execute(text(actual_q), parameters).fetchall()
                    else:
                        actual_result = conn.execute(text(actual_q), parameters).fetchall()
                else:
                    if algorithm_name == "Holo":
                        actual_result = conn2.execute(text(actual_q)).fetchall()
                    else:
                        actual_result = conn.execute(text(actual_q)).fetchall()

            except SQLAlchemyError as e:
                conn.rollback()
                skipped.append((idx, "actual_q_failed", str(e)))
                print(f"[SKIP] Query {idx} failed for {algorithm_name}: {e}")
                continue

            # ---- compute metrics only for successful queries ----
            expected_set = set(expected_result)

            if is_probabilistic:
                prob_entries = [tuple(row) for row in actual_result]
                prob_values = [float(row[-1]) for row in prob_entries]
                prob_rows = [tuple(row[:-1]) for row in prob_entries]

                sum_prob_correct = sum(p for row, p in zip(prob_rows, prob_values) if row in expected_set)
                sum_prob_wrong = sum(p for row, p in zip(prob_rows, prob_values) if row not in expected_set)
                sum_prob_total = sum(prob_values)

                if len(prob_rows) == 0:
                    exp_precision = 1.0
                    exp_noise = 0.0
                else:
                    if sum_prob_total > 0:
                        exp_precision = sum_prob_correct / sum_prob_total
                        exp_noise = sum_prob_wrong / sum_prob_total
                    else:
                        exp_precision = float("nan")
                        exp_noise = float("nan")

                exp_recall = sum_prob_correct / len(expected_set) if expected_set else 1.0
                true_positives = len(expected_set & set(prob_rows))
                coverage = true_positives / len(expected_set) if expected_set else 1.0

                results_with_truth_set.append((expected_set, prob_rows, prob_values))

            else:
                actual_set = set(actual_result)
                true_positives  = len(expected_set & actual_set)
                false_positives = len(actual_set - expected_set)

                total_actual    = len(expected_set)
                total_predicted = len(actual_set)

                exp_precision = true_positives / total_predicted if total_predicted > 0 else 1.0
                exp_recall    = true_positives / total_actual    if total_actual > 0 else 1.0
                exp_noise     = false_positives / total_predicted if total_predicted > 0 else 0.0
                coverage      = true_positives / len(expected_set) if expected_set else 1.0

            results.append((idx, exp_precision, exp_recall, coverage, exp_noise))

    return results, results_with_truth_set


def summarize_results(results):
    if not results:
        return 0.0, 0.0, 0.0, 0.0

    def finite(x):
        return x is not None and not (isinstance(x, float) and math.isnan(x)) and math.isfinite(x)

    prec = [p for _, p, _, _, _ in results if finite(p)]
    rec  = [r for _, _, r, _, _ in results if finite(r)]
    cov  = [c for _, _, _, c, _ in results if finite(c)]
    noi  = [n for _, _, _, _, n in results if finite(n)]
    avg_precision = sum(prec) / len(prec) if prec else float("nan")
    avg_recall    = sum(rec)  / len(rec)  if rec  else float("nan")
    avg_coverage  = sum(cov)  / len(cov)  if cov  else float("nan")
    avg_noise     = sum(noi)  / len(noi)  if noi  else float("nan")

    return avg_precision, avg_recall, avg_coverage, avg_noise


def compute_precision_recall_at_thresholds(results, thresholds=None):
    if thresholds is None:
        thresholds = np.arange(0.0, 1.00, 0.01)

    all_precision_at_p = {p: [] for p in thresholds}
    all_recall_at_p = {p: [] for p in thresholds}

    for truth_set, prob_rows, prob_values in results:
        for P in thresholds:
            selected = [(row, p) for row, p in zip(prob_rows, prob_values) if p > P]
            selected_rows = set(row for row, _ in selected)

            if not selected:
                prec = 0.0
                rec = 0.0
            else:
                tp = len(selected_rows & truth_set)
                prec = tp / len(selected_rows)
                rec = tp / len(truth_set) if truth_set else 1.0

            all_precision_at_p[P].append(prec)
            all_recall_at_p[P].append(rec)

    avg_precision = [np.mean(all_precision_at_p[p]) for p in thresholds]
    avg_recall = [np.mean(all_recall_at_p[p]) for p in thresholds]
    avg_f1 = [
        (2 * p * r) / (p + r) if (p + r) > 0 else 0.0
        for p, r in zip(avg_precision, avg_recall)
    ]
    return thresholds, avg_precision, avg_recall, avg_f1

def plot_precision_recall_at_p(thresholds, avg_precision, avg_recall, avg_f1,cqa_precision,cqa_recall):

    cqa_f1 = 2 * (cqa_precision * cqa_recall) / (cqa_precision + cqa_recall)

    # --- Precision@P ---
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_precision, marker='o', label='Precision@P (PRA)', color='blue')
    plt.axhline(y=cqa_precision, color='red', linestyle='--', label=f'CQA Precision ({cqa_precision:.4f})')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("Average Precision")
    plt.title("Precision at Probability Threshold P")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- Recall@P ---
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_recall, marker='s', label='Recall@P (PRA)', color='green')
    plt.axhline(y=cqa_recall, color='red', linestyle='--', label=f'CQA Recall ({cqa_recall:.4f})')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("Average Recall")
    plt.title("Recall at Probability Threshold P")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- F1@P ---
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_f1, marker='^', label='F1@P (PRA)', color='purple')
    plt.axhline(y=cqa_f1, color='red', linestyle='--', label=f'CQA F1 ({cqa_f1:.4f})')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("F1 Score")
    plt.title("F1 Score at Probability Threshold P")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



