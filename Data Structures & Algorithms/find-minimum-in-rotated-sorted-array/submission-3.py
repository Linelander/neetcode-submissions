class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: # can't be l. could be m. best on right side
                l = m + 1
            else: r = m # M can't be it. it could be L?

        return nums[l]