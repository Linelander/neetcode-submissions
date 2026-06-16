import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            print("stones: ", stones)
            stone1 = heapq.heappop(stones)
            heapq.heapify_max(stones)
            stone2 = heapq.heappop(stones)
            newstone = stone1 - stone2
            print("new stone: ", newstone)
            stones.append(newstone)
            heapq.heapify_max(stones)
        return stones[0]