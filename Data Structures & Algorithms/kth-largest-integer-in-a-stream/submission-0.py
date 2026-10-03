class KthLargest:

    def __init__(self, k: int, nums: List[int]):
         # Min-heap of size K - data structure with a sorted property
         self.minHeap, self.k = nums, k

         # turn the array into a min-heap
         heapq.heapify(self.minHeap)

         while len(self.minHeap) > k:
            # heapq.heappop() function removes and returns the smallest element from a heap. 
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Adds a new element to the heap while maintaining the heap property
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            # Removes and returns the smallest element from the heap
            heapq.heappop(self.minHeap)

        # return the minimum, always stored in the 0 index in heaps
        return self.minHeap[0]


