class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def recur(i, prev) -> int:
            if i in memo:
                return memo[i]
            
            best = 0
            
            for j in range(i, len(nums)):
                if nums[j] > prev:
                    best = max(best, 1 + recur(j, nums[j]))

            memo[i] = best
            return best

        return recur(0, float('-inf'))