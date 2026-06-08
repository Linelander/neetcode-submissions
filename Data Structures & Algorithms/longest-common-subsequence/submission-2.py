class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def recur(i, j) -> int:
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                return 1 + recur(i+1, j+1)

            res = 0    
            res += max(recur(i + 1, j), recur(i, j + 1))

            memo[(i, j)] = res
            return res
            
        return recur(0, 0)