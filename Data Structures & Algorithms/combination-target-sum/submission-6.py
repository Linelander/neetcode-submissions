class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        snums = sorted(nums)

        def backtrack(start, total):
            # if total > target:
            #     return
            if total == target:
                result.append(current[:])
                return

            for i in range(start, len(snums)):
                if snums[i] + total > target:
                    return
                current.append(snums[i])
                backtrack(i, total + snums[i])
                current.pop()

        backtrack(0, 0)
        return result