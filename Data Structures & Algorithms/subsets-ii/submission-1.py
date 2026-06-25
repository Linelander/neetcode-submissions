class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def recur(x, sub):
            result.append(sub[:])
            for i in range (x, len(nums)):
                if i > x and x < len(nums) and nums[i] == nums[i-1]: # was the last one the same?
                    continue
                sub.append(nums[i])
                recur(i + 1, sub[:])
                sub.pop()

        recur(0, [])
        return result