import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = [(0, k)]
        adj = defaultdict(list)
        for u, v, t in times: # adjacency list where index = source
            adj[u].append((v, t))
        bestD = {node: float('inf') for node in range(1, n+1)}
        bestD[k] = 0


        while pq:
            time, node = heapq.heappop(pq)
            if time > bestD[node]: 
                continue
                # for if we already found something better
            for neighbor, ntime in adj[node]:
                if time + ntime < bestD[neighbor]:
                    bestD[neighbor] = time + ntime
                    heapq.heappush(pq, (bestD[neighbor], neighbor))
                    # ^^^ push new finding

        ans = max(bestD.values()) # values are distances
        return ans if ans < float('inf') else -1

