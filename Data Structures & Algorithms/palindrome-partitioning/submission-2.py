class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []
        
        def isPal(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return
            
            for i in range(start, len(s)):
                # expand from current start
                prefix = s[start:i + 1]

                if isPal(prefix):
                    # recognize it as a palindrome...
                    path.append(prefix)
                    # and then importantly, MOVE ON
                    # this algorithm does not retread ground within a path
                    backtrack(i + 1)
                    path.pop()
                    # pop and then loop, experimenting with a different end point for the current palindrome search
        backtrack(0)
        return result

        