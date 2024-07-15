import heapq

# Min-Heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
print("Heap:", heap)

# Pop the smallest element
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)
print("Heap after pop:", heap)


# Heaps are a specialized tree-based data structure that satisfies the heap property. 
# A min-heap has the smallest element at the root, 
# while a max-heap has the largest element at the root.

