class Solution:
    def rob(self, nums: List[int]) -> int:
        hauls = nums[:] + [0] * 3

        print(hauls)

        for i in range(len(nums)-1, -1, -1):
            hauls[i] = hauls[i] + max(hauls[i+2], hauls[i+3])

        return max(hauls[0], hauls[1])

