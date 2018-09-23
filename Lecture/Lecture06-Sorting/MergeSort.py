def mergeSort(S):
    """Sort the elements of Python list S using the merge sort algorithm"""
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    mergeSort(S1)
    mergeSort(S2)
    merge(S1, S2, S)

def mergeSort_st(S):
    """Sort the elements of Python list S using the merge sort algorithm"""
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[1:mid]
    S2 = S[mid:n]
    mergeSort(S1)
    mergeSort(S2)
    merge(S1, S2, S)


def merge(S1, S2, S):
    """Merge two sorted Python Lists S1 and S2 into properly sized list S"""
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i = i+1
        else:
            S[i+j] = S2[j]
            j = j+1


alist = [54, 26, 93, 17, 77, 31, 44, 44,55, 20]
"""alist = [54, 26]"""
mergeSort(alist)
print("Sorted List ",alist)
