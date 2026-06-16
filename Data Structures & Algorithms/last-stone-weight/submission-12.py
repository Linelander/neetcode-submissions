import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heapq.heappush_max(stones, 
                heapq.heappop_max(stones) 
                - heapq.heappop_max(stones))
            heapq.heapify_max(stones)
        return stones[0]