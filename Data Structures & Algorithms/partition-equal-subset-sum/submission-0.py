class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def recur(i, remaining):
            if remaining == 0:
                return True
            if i >= len(nums) or remaining < 0:
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            result = recur(i + 1, remaining) or recur(i + 1, remaining - nums[i])
            memo[(i, remaining)] = result
            return result

        return recur(0, target)