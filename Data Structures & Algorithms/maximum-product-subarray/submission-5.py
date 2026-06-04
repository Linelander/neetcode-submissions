import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        maximum = float('-inf')

        for l in range(len(nums)):
            for r in range(l + 1, len(nums) + 1):
                if (l, r) not in memo:
                    memo[(l, r)] = math.prod(nums[l:r])
                maximum = max(maximum, memo[(l, r)])

        return maximum

