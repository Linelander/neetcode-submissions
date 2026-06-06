class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = False

        memo = {}

        def slicer(i):
            if (i == len(s)):
                return True

            if i in memo:
                return memo[i]

            result = False

            for word in wordDict:
                if s[i:i + len(word)] == word:
                    result = result or slicer(i + len(word))

            memo[i] = result
            return result
            
        return slicer(0)