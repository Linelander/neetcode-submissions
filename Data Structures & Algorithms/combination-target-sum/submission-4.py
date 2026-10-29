class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start):
            total = sum(current)
            if total > target:
                return
            if total == target:
                result.append(current[:])
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i)
                current.pop()

        backtrack(0)
        return result