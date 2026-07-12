import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim

        adj = [[] for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                manh = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((manh, j))
                adj[j].append((manh, i))

        # arbitrary starting point will justbe adj[0]

        heap = [(0, 0)] # (cost, point)
        visited = set()
        cost = 0

        # make heap with starting point
        # check in visited
        # add it to visited, acccumulate cost
        # get node's adjacency list
        # add all neighbors to heap if not visited

        while len(visited) < len(points):
            m, n = heapq.heappop(heap)
            if n in visited:
                continue
            visited.add(n)
            cost += m
            for manh, nxt in adj[n]:
                if nxt not in visited:
                    heapq.heappush(heap, (manh, nxt))

        return cost