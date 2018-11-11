from BinaryMinHeap import BinaryMinHeap as bh

heap = bh()

heap.heap_push(1)
heap.heap_push(2)
heap.heap_push(3)
heap.heap_push(4)
heap.heap_push(5)
heap.heap_push(6)
heap.heap_push(7)

heap.heap_pop(4)
heap.heap_pop(6)
heap.heap_pop(2)
heap.heap_pop(7)

assert(heap.table == [1,5,3])