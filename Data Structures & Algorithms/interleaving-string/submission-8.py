class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}


        def dp(i1, i2, i3):
            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)
            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]
            # oob?


            res = False
            if i1 < len(s1) and s3[i3] == s1[i1]:
                res |= dp(i1 + 1, i2, i3 + 1)
            if not res and i2 < len(s2) and s3[i3] == s2[i2]:
                res |= dp(i1, i2 + 1, i3 + 1)
            memo[(i1, i2, i3)] = res
            return res

        return dp(0, 0, 0)