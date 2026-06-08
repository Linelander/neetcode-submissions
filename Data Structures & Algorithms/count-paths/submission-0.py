class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def recur(i, j) -> int:
            print((i, j), "given: ", (m, n))
            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0

            if i+1 < m:
                print("hey i")
                res += recur(i + 1, j)
            if j+1 < n:
                print("hey j")
                res += recur(i, j + 1)

            memo[(i, j)] = res
            return res

        return recur(0, 0)