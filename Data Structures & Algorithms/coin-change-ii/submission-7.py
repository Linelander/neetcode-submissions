class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(knap: int, ic):
            if str(knap) + ',' + str(ic) in memo:
                return memo[str(knap) + ',' + str(ic)]
            
            if knap < 0:
                memo[str(knap) + ',' + str(ic)] = 0
                return 0
            elif knap == 0:
                memo[str(knap) + ',' + str(ic)] = 1
                return 1
            res = 0
            for i in range(ic, len(coins)):
                res += dfs(knap - coins[i], i)
            memo[str(knap) + ',' + str(ic)] = res
            return res
        
        return dfs(amount, 0)