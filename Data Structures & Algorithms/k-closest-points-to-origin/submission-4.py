import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eudis(x1, y1, x2, y2) -> int:
            return sqrt((x1 - x2)**2 + (y1 - y2)**2)

        heap = []
        for x, y in points:
            heapq.heappush(heap, [eudis(x, y, 0, 0), [x, y]])

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result