class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for row in range(l):
            for col in range(row, l):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        for row in matrix:
            row.reverse()