class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def step(i):
            if i >= n:
                return i == n # quantize to n
            if cache[i] != -1:
                return cache[i]
            cache[i] = step(i+1) + step(i+2)
            return cache[i]
        return step(0)