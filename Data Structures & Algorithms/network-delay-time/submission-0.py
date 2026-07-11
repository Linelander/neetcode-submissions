import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        
        adj = defaultdict(list)
        for u, v, t in times: # adjacency list where index = source
            adj[u].append((v, t))

        dist = {}
        pq = [(0, k)] # origin

        while pq:
            time, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = time
            for target, weight in adj[node]:
                if target not in dist:
                    heapq.heappush(pq, (time + weight, target))

        return max(dist.values()) if len(dist) == n else -1




