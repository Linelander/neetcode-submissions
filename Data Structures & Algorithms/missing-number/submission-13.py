class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        whole = sum(range(len(nums)+1))
        actual = sum(nums)
        return whole - actual