class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l + r) // 2
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            if matrix[i][j] == target: return True
            if matrix[i][j] < target:
                l = m+1
            else: r = m-1

        return False