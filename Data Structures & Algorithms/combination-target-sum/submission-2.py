class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start):
            if sum(current) > target:
                return
            if sum(current) == target:
                result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i)
                current.pop()

        backtrack(0)
        return result