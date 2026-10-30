class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def bt(start):
            if sum(current) > target:
                return
            if sum(current) == target:
                result.append(current[:])
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                bt(i)
                current.pop()

        bt(0)
        return result

