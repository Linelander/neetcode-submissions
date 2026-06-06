class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = False

        memo = {}

        def slicer(i):
            if (i == len(s)):
                return True

            # returning the memo should happen before anything else
            if i in memo:
                return memo[i]

            result = False

            for word in wordDict:
                if s[i:i + len(word)] == word:
                    result = result or slicer(i + len(word))

            # and assigning a memo should happen after everything else to cache
            # all possible results
            memo[i] = result
            return result
            
        return slicer(0)