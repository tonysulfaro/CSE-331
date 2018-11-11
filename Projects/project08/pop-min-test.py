from BinaryMinHeap import BinaryMinHeap as bh

heap = bh()

heap.heap_push(1)
heap.heap_push(2)
heap.heap_push(3)
heap.heap_push(4)
heap.heap_push(5)
heap.heap_push(6)
heap.heap_push(7)

heap.pop_min()

assert(heap.table == [2,4,3,7,5,6])

heap.pop_min()

assert(heap.table == [3,4,6,7,5])