from BinaryMinHeap import BinaryMinHeap as bh

heap = bh()

heap.heap_push(1)
heap.heap_push(2)
heap.heap_push(3)
heap.heap_push(4)
heap.heap_push(5)

assert(heap.get_size() == 5)
assert(heap.parent(4) == 1)
assert(heap.left_child(0) == 1)
assert(heap.right_child(0) == 2)
assert(heap.has_left(2) == False)
assert(heap.has_right(0) == True)