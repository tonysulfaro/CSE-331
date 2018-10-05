from linked_queue import LinkedQueue


def quick_sort_queue(S):
    """sort elements of queue S using quick sort"""

    n = len(S)
    if n < 2:
        return  # list is already sorted

    # divide
    pivot = S.first()  # use first element as the pivot

    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < pivot:
            L.enqueue(S.dequeue())
        elif pivot < S.first():
            G.enqueue(S.dequeue())
        else:  # val is equal to pivot
            E.enqueue(S.dequeue())

    # Conquer (with recursion)
    quick_sort_queue(L)  # sorts elements less than pivot
    quick_sort_queue(G)  # sorts elements greater than pivot

    # combine elements
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


my_queue = LinkedQueue()
my_queue.enqueue(3)
my_queue.enqueue(67)
my_queue.enqueue(32)
my_queue.enqueue(1)
my_queue.enqueue(0)
my_queue.enqueue(8)
my_queue.enqueue(9)

quick_sort_queue(my_queue)
