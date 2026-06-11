class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        setrows = []        # i
        setcols = []        # j

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setrows.append(i)
                    setcols.append(j)

        for row in setrows:
            for x in range(len(matrix[row])):
                matrix[row][x] = 0

        for col in setcols:
            for x in range(len(matrix)):
                matrix[x][col] = 0