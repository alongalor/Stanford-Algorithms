def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        p = A[0]
        i = 1
        for j in range(1,len(A)):
            if A[j] < p:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[0], A[i-1] = A[i-1], A[0]
        A[:i-1], A[i:] = quicksort(A[:i-1]), quicksort(A[i:])
        return A