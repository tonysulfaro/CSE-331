from Stack import Stack


def main():
    stack = Stack()
    stack.push(0)

    assert stack.data == [0, None]
    assert stack.capacity == 2
    assert stack.size == 1

    stack.push(1)
    assert stack.data == [0, 1]
    assert stack.capacity == 2
    assert stack.size == 2

    stack.push(2)
    assert stack.data == [0, 1, 2, None]
    assert stack.capacity == 4
    assert stack.size == 3

    stack.push(3)
    assert stack.data == [0, 1, 2, 3]
    assert stack.capacity == 4
    assert stack.size == 4

    print("Expected:", "['0', '1', '2', '3'] Capacity: 4")
    print("Output:", str(stack))


main()