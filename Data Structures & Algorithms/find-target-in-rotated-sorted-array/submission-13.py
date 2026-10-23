class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rules for this revisit: see if you can solve it
        # without rearranging the array

        l, r = 0, len(nums) - 1

        while l < r:
            m = (r+l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                

        pivot = l

        def bsearch(left: int, right: int) -> int:
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
        result = bsearch(0, pivot - 1)
        if result != -1:
            return result
        return bsearch(pivot, len(nums) - 1)