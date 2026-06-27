class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        big = float('-inf')
        for i in range(len(nums)):
            curr += nums[i]
            big = max(big, curr)

            if curr < 0:
                curr = 0

        return big
            