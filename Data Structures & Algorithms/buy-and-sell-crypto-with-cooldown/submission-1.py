class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
    
        def dfs(i, buying: bool):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[i, buying]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, buying)
                memo[(i, buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return dfs(0, True)