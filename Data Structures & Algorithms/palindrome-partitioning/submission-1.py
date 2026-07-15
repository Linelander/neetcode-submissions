class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []

        def isPal(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):
                result.append(path[:]) # don't forget :
                return

            for i in range(start, len(s)):
                prefix = s[start:i + 1] # always use +1
                if isPal(prefix):
                    path.append(prefix)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return result