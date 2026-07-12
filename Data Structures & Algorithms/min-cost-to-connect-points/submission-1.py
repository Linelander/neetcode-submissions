class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                manh = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((manh, i, j))
        edges.sort()

        parent = list(range(len(points)))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        krus = 0

        for m, a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb: continue
            parent[ra] = rb
            krus += m

        return krus