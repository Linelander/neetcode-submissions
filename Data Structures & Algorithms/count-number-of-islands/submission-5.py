from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        result += 1
                        q = deque()

                        def visit(y, x):
                            grid[y][x] = "0"
                            q.append([y, x])

                        q.append([i, j])
                        while q:
                            pl = q.popleft()
                            qi, qj = pl[0], pl[1]

                            if qi+1 < len(grid)     and grid[qi+1][qj] == "1":
                                visit(qi+1, qj)
                            if qi-1 >= 0            and grid[qi-1][qj] == "1":
                                visit(qi-1, qj)
                            if qj+1 < len(grid[0])  and grid[qi][qj+1] == "1":
                                visit(qi, qj+1)
                            if qj-1 >= 0            and grid[qi][qj-1] == "1":
                                visit(qi, qj-1)

        return result



