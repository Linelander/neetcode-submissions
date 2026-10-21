class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(bal: int):
            if bal in memo:
                return memo[bal]
            if bal == 0:
                return 0
            
            result = float('+inf')
            for coin in coins:
                if (bal - coin) >= 0:
                    result = min(result, 1 + dfs(bal - coin))
                    memo[bal] = result
            return result

        res = dfs(amount)
        return res if res != float('+inf') else -1