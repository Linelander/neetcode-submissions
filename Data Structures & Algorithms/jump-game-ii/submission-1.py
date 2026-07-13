class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            
            result = float('inf')
            for ni in range(i+1, i+nums[i] + 1):
                result = min(result, 1 + dfs(ni))
            memo[i] = result
            return result

        return dfs(0)