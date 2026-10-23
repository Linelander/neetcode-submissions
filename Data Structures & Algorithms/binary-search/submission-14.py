class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rules for this revisit: see if you can solve it
        # without rearranging the array

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            # if nums[m] < nums[l]: #it's not sorted yet. what do we do?
            #     # ???
            else: # normal binary search
                if target > nums[m]:
                    l = m+1
                else:
                    r = m-1

        return -1