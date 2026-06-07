class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def recur(i, prev) -> int:
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            best = 0
            
            for j in range(i, len(nums)):
                if nums[j] > prev:
                    best = max(best, 1 + recur(j, nums[j]))

            memo[(i, prev)] = best
            return best

        return recur(0, float('-inf'))