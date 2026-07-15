class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:          # left half sorted
                if nums[l] <= target < nums[m]: # is it there?
                    r = m - 1 # then go there
                else:
                    l = m + 1 # otherwise go the other way
                # eventually we will narrow it down to a sorted half
            else:                            # right half must be sorted
                if nums[m] < target <= nums[r]: # is it there?
                    l = m + 1
                else:
                    r = m - 1
        return -1