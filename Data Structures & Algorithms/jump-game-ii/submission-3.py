class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0

        steps = 0
        while r < len(nums) - 1:
            nr = r
            for i in range (l, r + 1):
                nr = max(nr, i + nums[i])
            l = r+1
            r = nr
            steps += 1

        return steps