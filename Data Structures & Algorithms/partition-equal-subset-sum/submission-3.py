class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}

        if total % 2 != 0:
            return False

        target = total // 2

        def recur(i, remaining):
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            if i >= len(nums) or remaining < 0:
                return False
            
            if remaining == 0:
                return True

            memo[(i, remaining)] = recur(i+1, remaining) or recur(i+1, remaining-nums[i])
            return memo[(i, remaining)]

        return recur(0, target)