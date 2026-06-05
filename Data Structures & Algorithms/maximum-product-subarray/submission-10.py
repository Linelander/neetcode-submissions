import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        maximum = float('-inf')

        for l in range(len(nums)):
            running = 1
            for r in range(l + 1, len(nums) + 1):
                running *= nums[r - 1]
                maximum = max(maximum, running)

        return maximum