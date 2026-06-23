class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(x, sub):
            
            sub.append(nums[x])
            result.append(sub[:])

            for i in range(x+1, len(nums)):
                recur(i, sub[:])
        
        for i in range(len(nums)):
            recur(i, [])
        result.append([])
        return result
        