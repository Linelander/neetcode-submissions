class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        haul = [-1] * len(nums)

        def rob(i, toEnd):
            if toEnd:
                if i >= len(nums):
                    return 0
            elif i >= len(nums) - 1:
                return 0
            if haul[i] != -1:
                return haul[i]
            haul[i] = max(nums[i] + rob(i+2, toEnd), rob(i+1, toEnd)) # need to be able to skip
            return haul[i]

        max0 = rob(0, False)
        haul = [-1] * len(nums)
        max1 = rob(1, True)
        return max(max0, max1)