from Stack import Stack
from Stack import reverse


def main():
    stack = Stack()
    for i in range(0, 4):
        stack.push(i)

    assert stack.data == [0, 1, 2, 3]
    assert stack.size == 4
    assert stack.capacity == 4

    stack = reverse(stack)

    print("Output: ", str(stack))
    print("Expected: ['3', '2', '1', '0'] Capacity: 4")

    assert stack.data == [3, 2, 1, 0]
    assert stack.size == 4
    assert stack.capacity == 4


main()