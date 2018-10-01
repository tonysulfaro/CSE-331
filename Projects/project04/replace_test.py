from Stack import Stack
from Stack import replace


def main():
    stack = Stack()
    for i in range(0, 4):
        stack.push(i)

    assert stack.data == [0, 1, 2, 3]
    assert stack.size == 4
    assert stack.capacity == 4

    stack = replace(stack, 0, 100)

    print("Output: ", str(stack))
    print("Expected: ['100', '1', '2', '3'] Capacity: 4")

    assert stack.data == [100, 1, 2, 3]
    assert stack.size == 4
    assert stack.capacity == 4


main()