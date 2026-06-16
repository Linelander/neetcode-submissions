import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            newstone = stone1 - stone2
            heapq.heappush_max(stones, newstone)
            heapq.heapify_max(stones)
        return stones[0]