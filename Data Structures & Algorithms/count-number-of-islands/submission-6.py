from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                    if grid[i][j] != "1":
                        continue
                    result += 1
                    q = deque()

                    def visit(y, x):
                        if 0 <= y < rows and 0 <= x < cols and grid[y][x] == "1":
                            grid[y][x] = "0"
                            q.append([y, x])

                    visit(i, j)
                    while q:
                        pi, pj = q.popleft()
                        for oi, oj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            visit(pi + oi, pj + oj)

        return result

