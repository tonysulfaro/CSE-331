from Stack import Stack


def main():
    stack = Stack()

    assert stack.is_empty() == True

    stack.push(1)
    assert stack.is_empty() == False

    stack.pop()
    assert stack.is_empty() == True


main()