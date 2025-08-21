from src.database.fetch_data import *
from sqlalchemy import text
import numpy as np
import matplotlib.pyplot as plt

def load_queries_by_blank_lines(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    query_blocks = [q.strip() for q in content.split('\n\n') if q.strip()]
    return query_blocks

def calculate_expected_values(query_file_name_expected, query_file_name_actual, engine):

    is_probabilistic = "prob" in query_file_name_actual.lower()

    expected_queries = load_queries_by_blank_lines(query_file_name_expected)
    actual_queries = load_queries_by_blank_lines(query_file_name_actual)

    if len(expected_queries) != len(actual_queries):
        raise ValueError(f"Mismatch in number of queries: truth={len(expected_queries)}, prob={len(actual_queries)}")

    results = []
    results_with_truth_set = []
    with engine.connect() as conn:
        for idx, (expected_q, actual_q) in enumerate(zip(expected_queries, actual_queries), start=1):

            expected_result = conn.execute(text(expected_q)).fetchall()
            actual_result = conn.execute(text(actual_q)).fetchall()

            expected_set = set(expected_result)
            if is_probabilistic:
                prob_entries = [tuple(row) for row in actual_result]
                prob_values = [float(row[-1]) for row in prob_entries]
                prob_rows = [tuple(row[:-1]) for row in prob_entries]
                sum_prob_correct = sum(p for row, p in zip(prob_rows, prob_values) if row in expected_set)
                sum_prob_wrong = sum(p for row, p in zip(prob_rows, prob_values) if row not in expected_set)
                sum_prob_total = sum(prob_values)

                exp_precision = sum_prob_correct / sum_prob_total if sum_prob_total > 0 else 0.0
                exp_recall = sum_prob_correct / len(expected_set) if expected_set else 1.0
                exp_noise = sum_prob_wrong / sum_prob_total if sum_prob_total > 0 else 0.0
                true_positives = len(expected_set & set(prob_rows))
                coverage = true_positives / len(expected_set)
                results_with_truth_set.append((expected_set,prob_rows,prob_values))

            else:
                actual_set = set(actual_result)
                true_positives = len(expected_set & actual_set)
                false_positives = len(actual_set - expected_set)
                total_actual = len(expected_set)
                total_predicted = len(actual_set)
                exp_precision = true_positives / total_predicted if total_predicted > 0 else 0.0
                exp_recall = true_positives / total_actual if total_actual > 0 else 1.0
                exp_noise = false_positives / total_predicted if total_predicted > 0 else 0.0
                coverage = true_positives / len(expected_set)
            results.append((idx, exp_precision, exp_recall, coverage, exp_noise))

    return results,results_with_truth_set

def summarize_results(results):
    if not results:
        return 0.0, 0.0

    total_precision = sum(p for _, p, _, _, _ in results)
    total_recall = sum(r for _, _, r, _, _ in results)
    total_coverage = sum(r for _, _, _, r, _ in results)
    total_noise = sum(r for _, _, _, _, r in results)
    n = len(results)

    avg_precision = total_precision / n
    avg_recall = total_recall / n
    avg_coverage = total_coverage / n
    avg_noise = total_noise / n

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


def plot_precision_recall_at_p(thresholds, avg_precision, avg_recall, avg_f1):

    # Precision@P
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_precision, marker='o', label='Precision@P', color='blue')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("Average Precision")
    plt.title("Precision at Probability Threshold P")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Recall@P
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_recall, marker='s', label='Recall@P', color='green')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("Average Recall")
    plt.title("Recall at Probability Threshold P")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # F1@P
    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, avg_f1, marker='^', label='F1@P', color='purple')
    plt.xlabel("Probability Threshold (P)")
    plt.ylabel("F1 Score")
    plt.title("F1 Score at Probability Threshold P")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


