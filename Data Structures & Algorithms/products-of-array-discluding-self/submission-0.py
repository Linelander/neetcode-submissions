class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()

        for i in range(len(nums)):
            if i > 0:
                prefix[i] = prefix[i] * prefix[i-1]

        for i in reversed(range(len(nums))):
            if i < len(nums) - 1:
                suffix[i] = suffix[i] * suffix[i+1]

        # print(prefix)
        # print(suffix)

        result = [1] * len(nums);
        for i in range(len(nums)):
            if i > 0:
                result[i] *= prefix[i - 1] 
            if i < len(nums) - 1:
                result[i] *= suffix[i + 1]

        return result