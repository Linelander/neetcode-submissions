class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = r // 2

        while l <= r:
            m = (r+l) // 2
            if nums[m] > target:
                print("left")
                r = m-1
            elif nums[m] < target:
                print("right")
                l = m+1
            else: return m

        return -1