class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 2)]   # index 1 = buying, 0 = selling
                                                        # rows n and n+1 are the base case

        print(dp)


        for i in range(len(prices) - 1, -1, -1): # go backwards
            dp[i][1] = max(dp[i+1][1], dp[i+1][0] - prices[i])
            dp[i][0] = max(dp[i+1][0], dp[i+2][1] + prices[i])

        return dp[0][1]