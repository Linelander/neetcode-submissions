class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(knap: int, ic):
            if (knap, ic) in memo:
                return memo[(knap, ic)]
            
            if knap < 0:
                memo[(knap, ic)] = 0
                return 0
            elif knap == 0:
                memo[(knap, ic)] = 1
                return 1
            res = 0
            for i in range(ic, len(coins)):
                res += dfs(knap - coins[i], i)
            memo[(knap, ic)] = res
            return res
        
        return dfs(amount, 0)