from Stack import Stack


def main():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.data == [0, 1, 2, 3]
    assert stack.capacity == 4
    assert stack.size == 4

    popped = stack.pop()
    assert popped == 3

    popped = stack.pop()
    assert popped == 2

    print(stack)

    assert stack.data == [0, 1]
    assert stack.capacity == 2
    assert stack.size == 2

    print("Expected:", "['0', '1'] Capacity: 2")
    print("Output:", str(stack))


main()