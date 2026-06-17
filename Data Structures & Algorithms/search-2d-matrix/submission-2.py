class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        all = []
        for lst in matrix: all += lst
        l = 0
        r = len(all) - 1
        while l <= r:
            m = (l + r) // 2
            if all[m] == target: return True
            if all[m] < target:
                l = m+1
            else: r = m-1

        return False