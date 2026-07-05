from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        seen = set()
        time = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    seen.add((i, j))
                    dq.append((i, j))

        def goodcoord(t):
            return (0 <= t[0] < len(grid) and 0 <= t[1] < len(grid[0]))

        def bfs(q):
            nonlocal time
            while q:
                for _ in range(len(q)):
                    cell = q.popleft()
                    if grid[cell[0]][cell[1]] == 1:
                        grid[cell[0]][cell[1]] = 2
                    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                        neighbor = (cell[0] + di, cell[1] + dj)
                        if (goodcoord(neighbor) and neighbor not in seen
                                and grid[neighbor[0]][neighbor[1]] == 1):
                            seen.add(neighbor)
                            q.append(neighbor)
                time += 1

        bfs(dq)

        for row in grid:
            if 1 in row:
                return -1
        return max(time, 0)