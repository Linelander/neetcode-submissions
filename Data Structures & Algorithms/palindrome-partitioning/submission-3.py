class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path, result = [], []

        def isPal(s):
            return s == s[::-1]

        def bt(start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                prefix = s[start:i + 1]
                if isPal(prefix):
                    path.append(prefix)
                    bt(i + 1)
                    path.pop()

        bt(0)
        return result