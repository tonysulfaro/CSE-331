import HybridSort as hs
from random import shuffle, seed


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
    print(hs.merge_sort(unsorted, 3, False))


if __name__ == "__main__":
    main()
