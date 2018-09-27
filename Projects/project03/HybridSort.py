"""
PROJECT 3 - Hybrid Sort
Name: Tony Sulfaro
PID: A52995491
"""


def merge_sort(unsorted, threshold, reverse):
    """
    Use Merge sort to sort big data
    :param unsorted: unsorted data to be sorted
    :param threshold: size at which to use insertion sort
    :param reverse: specifies ascending or descending for sorted list
    :return: sorted list
    """
    size = len(unsorted)

    if size < threshold:
        insertion_sort(unsorted, reverse)  # Use insertion sort for sub lists
        return unsorted

    if size < 2:
        return unsorted  # base case
    else:
        middle = size // 2
        list1 = merge_sort(unsorted[:middle], threshold, reverse)  # Divide list by //2 and run again
        list2 = merge_sort(unsorted[middle:], threshold, reverse)
        return merge(list1, list2, reverse)


def merge(list1, list2, reverse):
    """
    Merge two sorted lists into one
    :param list1: first sorted list
    :param list2: second sorted list
    :param reverse: weather or not to sort in descending order
    :return: New sorted list new_list
    """
    i = j = 0
    new_list = list1 + list2

    if reverse:  # thought about putting this check within the while loop but that is expensive.
        while i + j < len(new_list):
            if j == len(list2) or (i < len(list1) and list1[i] > list2[j]):  # greater put in new list
                new_list[i + j] = list1[i]
                i = i + 1
            else:
                new_list[i + j] = list2[j]
                j = j + 1
        return new_list

    while i + j < len(new_list):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):  # lesser put in new list
            new_list[i + j] = list1[i]
            i = i + 1
        else:
            new_list[i + j] = list2[j]
            j = j + 1
    return new_list


def insertion_sort(unsorted, reverse):
    """
    Sort a list in place
    :param unsorted: unsorted list to sort in place
    :param reverse: bool of weather to sort in ascending or descending order
    :return: None:
    """
    size = len(unsorted)

    if reverse:
        for i in range(1, size):
            j = i
            while (j > 0) and (unsorted[j] > unsorted[j - 1]):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]  # basically swap function
                j -= 1
    else:
        for i in range(1, size):
            j = i
            while (j > 0) and (unsorted[j] < unsorted[j - 1]):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
