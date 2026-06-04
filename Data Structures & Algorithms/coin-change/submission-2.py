class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            memo = {}
            
            def dfs(amount) -> int:
                if amount == 0: return 0
                if amount in memo: return memo[amount]

                result = float('inf')
                for coin in coins:
                    if amount - coin >= 0:
                        # the +1 counts THIS coin
                        result = min(result, 1 + dfs(amount - coin))
                memo[amount] = result
                return result
            
            result = dfs(amount)

            if result == float('inf'): return -1
            return result
        