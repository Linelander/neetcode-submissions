import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for num in nums:
            dd[num] += 1
        heap = [(-count, key) for key, count in dd.items()]
        heapq.heapify(heap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result