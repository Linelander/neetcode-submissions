class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # at each step: decide whether to include or exclude current value

        # if including, try plussing and minusing
            # does this handle the first space? because the first tihng you land on has to become positive

        # also need to consider if current adds up to target


        # maybe we just require that at least one of them be positive?

        memo = {}

        def bt(i, running):
            if i == len(nums):
                return running == 0
            if (i, running) in memo:
                return memo[(i, running)]

            ways = 0
            ways += bt(i+1, running - nums[i])    # sub
            ways += bt(i+1, running + nums[i])    # add

            memo[(i, running)] = ways
            return memo[(i, running)]

        return bt(0, target)