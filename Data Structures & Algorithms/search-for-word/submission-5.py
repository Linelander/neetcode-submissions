class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        
        def bt(startI, startJ, wip: str):            
            if startI < 0 or startJ < 0:
                return False
            if startI >= len(board) or startJ >= len(board[0]):
                return False

            original = wip
            wip += board[startI][startJ] # oob?
            
            if wip == word: return True

            # print(wip)

            seen.add((startI, startJ))

            success = False

            for offI, offJ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (startI + offI, startJ + offJ) not in seen:
                    success = success or bt(startI + offI, startJ + offJ, wip)

            # undo str and seen
            wip = original
            seen.remove((startI, startJ))

            return success

        success = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    success = success or bt(i, j, "")

        return success