def inv_count_brute_force(lst):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if (i<j) & (lst[i]>lst[j]):
                rslt.append((lst[i], lst[j]))
    return len(rslt)