class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []
        
        def isPal(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return
            for i in range(start, len(s)): # prefix sweep
                prefix = s[start:i+1]
                if isPal(prefix):
                    path.append(prefix)
                    backtrack(i+1) # this is the part that confuses me, along with the loop
                    path.pop()

        backtrack(0)
        return result
