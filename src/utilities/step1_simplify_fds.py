def simplify_FDs(fd_constraints):
    simplified = []
    for lhs, rhs_list in fd_constraints:
        for rhs in rhs_list:
            simplified.append((lhs, [rhs]))
    return simplified