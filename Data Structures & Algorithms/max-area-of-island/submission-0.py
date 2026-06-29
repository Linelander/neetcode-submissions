class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # this is the same as that island "poisoning" question

        def poison(pi, pj):
            if (pi < 0 or pi >= len(grid)
                or pj < 0 or pj >= len(grid[0])
                or grid[pi][pj] != 1):
                return 0
            grid[pi][pj] = 0
            result = 1
            result += poison(pi + 1, pj)
            result += poison(pi - 1, pj)
            result += poison(pi, pj - 1)
            result += poison(pi, pj + 1)
            return result
            
        res = float('-inf')

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, poison(i, j))

        return res