import HybridSort as hs
from random import shuffle, seed


def main():
    seed(1)
    unsorted = [i for i in range(500)] + [0, 1, 498, 499]
    threshold = 10
    reverse = True
    shuffle(unsorted)
    solution = sorted(unsorted)[::-1]

    unsorted = hs.merge_sort(unsorted, threshold, reverse)

    print(unsorted)
    print(solution)

    assert unsorted == solution


if __name__ == "__main__":
    main()