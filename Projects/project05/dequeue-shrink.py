from CircularQueue import CircularQueue


def main():
    test = CircularQueue(15)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)
    test.enqueue(3)

    print(test)

    print('REMOVE')

    test.dequeue()
    test.dequeue()
    test.enqueue(5)
    test.enqueue(5)
    test.enqueue(5)
    test.enqueue(5)
    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.dequeue()
    test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()
    # test.dequeue()

    print(test)


if __name__ == '__main__':
    main()
