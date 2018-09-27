def merge_sort(unsorted, threshold, reverse):
    """
    Use Merge sort to sort big data
    :param unsorted:
    :param threshold:
    :param reverse:
    :return:
    """
    n = len(unsorted)

    if n < threshold:
        insertion_sort(unsorted, reverse)
        return unsorted

    if n < 2:
        return unsorted
    else:
        middle = n // 2
        a = merge_sort(unsorted[:middle], threshold, reverse)
        b = merge_sort(unsorted[middle:], threshold, reverse)
        return merge(a, b, reverse)


def merge(S1, S2, reverse):
    """
    Merge two sorted lists into one
    :param S1: first sorted list
    :param S2: second sorted list
    :param reverse: weather or not to sort in descending order
    :return: New sorted list S
    """
    i = j = 0
    S = S1 + S2

    if reverse:
        while i + j < len(S):
            if j == len(S2) or (i > len(S1) and S1[i] > S2[j]):
                S[i + j] = S1[i]
                i = i + 1
            else:
                S[i + j] = S2[j]
                j = j + 1
        return S
    else:
        while i + j < len(S):
            if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                S[i + j] = S1[i]
                i = i + 1
            else:
                S[i + j] = S2[j]
                j = j + 1
        return S


def insertion_sort(unsorted, reverse):
    """
    Sort a list in place
    :param unsorted: unsorted list to sort in place
    :param reverse: bool of weather to sort in ascending or descending order
    :return: None:
    """
    n = len(unsorted)

    if reverse:
        for i in range(1, n):
            j = i
            while (j > 0) and (unsorted[j] > unsorted[j - 1]):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
    else:
        for i in range(1, n):
            j = i
            while (j > 0) and (unsorted[j] < unsorted[j - 1]):
                exchange(unsorted, j, j - 1)
                j -= 1


def exchange(a, i, j):
    """
    Exchange two variables
    Just gonna take this lecture code because its free real estate
    :param a: list
    :param i: index of item to compare
    :param j: index of previous item to compare
    :return: sorted list
    """
    a[i], a[j] = a[j], a[i]


def main():

    unsorted = [2, 1, 5, 3, 7, 2]
    print(unsorted)

    # print('in order')
    # insertion_sort(unsorted, False)
    # print(unsorted)
    #
    # print('revserse')
    # insertion_sort(unsorted, True)
    # print(unsorted)

    # insertion_sort(unsorted, True)
    # print(unsorted)

    print('merge sort')
    print(merge_sort(unsorted, 3, True))


if __name__ == "__main__":
    main()
