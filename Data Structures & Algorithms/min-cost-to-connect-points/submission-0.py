class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # use kruskal for minimum cost spanning tree
        # assume that all points are connected by edges
        # maybe just generate an adj list with manhattan distance
        # between all points

        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                manh = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((manh, i, j))  # this version stores indices of points
                                            # not actual coords
        edges.sort()

        parent = list(range(len(points)))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        krus = 0

        # kruskal
        for man, a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb: continue
            parent[ra] = rb # join in parent
            # add to kruskal
            krus += man

        return krus

