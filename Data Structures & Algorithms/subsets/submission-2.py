class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(x, sub):
            result.append(sub[:])
            for i in range(x, len(nums)):
                sub.append(nums[i])
                recur(i + 1, sub)
                sub.pop()
        
        recur(0, [])
        return result
        