class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount) -> int:
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0

            result = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + dfs(amount - coin))
            memo[amount] = result
            return result

        final = dfs(amount)
        if final == float('inf'): return -1
        return final