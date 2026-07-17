class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def knap(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining == 0:
                return 0

            result = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    result = min(result, 1 + knap(remaining - coin))
            memo[remaining] = result
            return result

        final = knap(amount)
        if final != float('inf'): return final
        return -1