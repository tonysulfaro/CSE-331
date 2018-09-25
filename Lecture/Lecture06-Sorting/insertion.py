def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]


def sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j - 1]):
            exchange(a, j, j - 1)
            j -= 1


def main():
    a = [8, 2, 4, 9, 6, 3]
    sort(a)
    print(a)
    b = [1, 2, 3, 4, 5, 6]
    sort(b)
    print(b)


if __name__ == '__main__': main()
