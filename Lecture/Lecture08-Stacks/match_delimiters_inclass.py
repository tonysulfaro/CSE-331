from array_stack_inclass import ArrayStack


def is_matched(expr):
    lefty = '[{('
    righty = ']})'
    S = ArrayStack()

    for value in expr:
        if value in lefty:
            S.push(value)
        elif value in righty:
            if S.is_empty():
                return False
            if righty.index(value) != lefty.index(S.pop()):
                return False

    return S.is_empty()


if __name__ == '__main__':
    print(is_matched('()[]['))
