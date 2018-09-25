def merge_sort(unsorted, threshold, reverse):
    """
    Use Merge sort to sort big data
    :param unsorted:
    :param threshold:
    :param reverse:
    :return:
    """

    n = len(unsorted)
    if n < 2:
        return
    mid = n // 2
    S1 = unsorted[0:mid]
    S2 = unsorted[mid:n]
    merge_sort(S1, threshold, reverse)
    merge_sort(S2, threshold, reverse)
    unsorted = merge(S1, S2, reverse)


def merge(first, second, reverse):
    """
    Merge two sorted lists into one
    :param first: first sorted list
    :param second: second sorted list
    :param reverse: weather or not to sort in descending order
    :return: New sorted list S
    """
    i = j = 0
    S = []

    if reverse:
        pass
    else:
        while i + j < len(S):
            if j == len(second) or (i < len(first) and first[i] < second[j]):
                S[i + j] = first[i]
                i = i + 1
            else:
                S[i + j] = second[j]
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
                unsorted[i], unsorted[j-1] = unsorted[j-1], unsorted[i]
                j -= 1


def main():
    print('sorting time')
    print('insert sort')

    unsorted = [2, 1, 5, 3, 7]
    print(unsorted)

    print('in order')
    insertion_sort(unsorted, False)
    print(unsorted)

    print('revserse')
    insertion_sort(unsorted, True)
    print(unsorted)


if __name__ == "__main__":
    main()
