class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if nums[len(nums) - 1] != len(nums):
            return len(nums)

        last = -1
        result = -1
        for n in nums:
            if n > last + 1:
                result = last + 1
            last = n
        return result

        # so why do we need XOR for this?