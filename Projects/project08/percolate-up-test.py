from BinaryMinHeap import BinaryMinHeap as bh

heap = bh()

heap.heap_push(7)
heap.heap_push(6)
heap.heap_push(5)
heap.heap_push(4)
heap.heap_push(3)
heap.heap_push(2)
heap.heap_push(1)

assert(heap.table == [1,4,2,7,5,6,3])