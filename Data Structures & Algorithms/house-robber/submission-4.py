class Solution:
    def rob(self, nums: List[int]) -> int:
        guide = [-1] * len(nums)
        def rob(i):
            if i >= len(nums):
                return 0
            if guide[i] != -1:
                return guide[i]
            guide[i] = nums[i] + max(rob(i + 2), rob(i + 3))
            return guide[i]
        
        return max(rob(0), rob(1))