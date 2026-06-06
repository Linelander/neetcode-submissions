import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxhere = minhere = result = nums[0]
        for x in nums[1:]:
            candidates = (x, x * maxhere, x * minhere)
            maxhere = max(candidates)
            minhere = min(candidates)
            result = max(result, maxhere)
        return result