class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        if nums[len(nums) - 1] != len(nums):
            return len(nums)
        
        result = -1
        for i in range(len(nums)):
            if nums[i] ^ i != 0:
                result = i
                break
        return result