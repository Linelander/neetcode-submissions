import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sudoku number
        # appearances
        # coords

        # we need to find...

        rowdicts    = [defaultdict(int) for _ in range(9)]
        columndicts = [defaultdict(int) for _ in range(9)]
        squaredicts = [[defaultdict(int) for _ in range(3)] for _ in range(3)]

        for i in range (9): # row
            for j in range (9): # column in row
                val = board[i][j]
                if (val == "." or val == ","):
                    continue
                
                # count val in current row dict
                if rowdicts[i][val] == 0:
                    rowdicts[i][val] += 1
                else:
                    print("rowfail")
                    return False

                
                # count val in current column dict
                if columndicts[j][val] == 0:
                    columndicts[j][val] += 1
                else:
                    print("columnfail")
                    return False

                # square dict too
                # 9 indices. come up with a mapping
                sq_row = i // 3
                sq_col = j // 3

                if (squaredicts[sq_row][sq_col])[val] == 0:
                    (squaredicts[sq_row][sq_col])[val] += 1
                else:
                    print("squarefail")
                    return False


        return True
        