class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # there's no maxHeap, so we use minHeap then negate the values.
        # By multiplying numbers by -1, the largest absolute number
        # becomes the smallest negative number, positioning it at the
        # top of a standard min-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
