class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def recur(x):
            if x >= len(cost):
                return 0
            if x in memo:
                return memo[x]
            memo[x] = cost[x] + min(recur(x+1), recur(x+2))
            return memo[x]

        return min(recur(0), recur(1))