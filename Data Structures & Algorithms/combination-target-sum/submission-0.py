class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(state: List[int], start: int):
            if sum(state) == target:
                result.append(state[:])
                return
            elif sum(state) > target: return

            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(state, i)
                state.pop()

        backtrack([], 0)
        return result
