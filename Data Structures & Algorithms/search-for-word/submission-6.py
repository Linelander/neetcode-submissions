class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def validIJ(i, j) -> bool:
            if i < 0 or j < 0:
                return False
            if i >= len(board) or j >= len(board[0]):
                return False
            return True
        
        def bt(startI, startJ, wip: str, depth):            
            # if startI < 0 or startJ < 0:
            #     return False
            # if startI >= len(board) or startJ >= len(board[0]):
            #     return False

            original = wip
            wip += board[startI][startJ] # oob?
            
            if wip == word: return True

            # print(wip)

            seen.add((startI, startJ))

            success = False

            for offI, offJ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newI = startI + offI
                newJ = startJ + offJ
                if ((newI, newJ) not in seen
                    and validIJ(newI, newJ)
                    and depth + 1 < len(word)
                    and board[newI][newJ] == word[depth + 1]):
                    success = success or bt(newI, newJ, wip, depth + 1)

            # undo str and seen
            wip = original
            seen.remove((startI, startJ))

            return success

        success = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    success = success or bt(i, j, "", 0)

        return success