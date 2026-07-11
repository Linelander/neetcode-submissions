class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfsSave(xi, xj):
            if board[xi][xj] != 'O':
                return

            board[xi][xj] = 'S'

            for di, dj in dirs:
                ni, nj = xi + di, xj + dj
                if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
                    continue
                dfsSave(ni, nj)

        # call for each thing on the border
        m, n = len(board), len(board[0])
        for i in range(m):
            dfsSave(i, 0)
            dfsSave(i, n - 1)
        for j in range(n):
            dfsSave(0, j)
            dfsSave(m - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'