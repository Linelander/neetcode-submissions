class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = [-1] * len(s)

        def dfs(i) -> int:
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if cache[i] != -1: return cache[i]

            result = 0
            result += dfs(i+1)
            if (i < len(s) - 1 
                and int(s[i:i+2]) >= 10 
                and int(s[i:i+2]) <= 26): 
                result += dfs(i + 2)
            cache[i] = result
            return result

        return dfs(0)