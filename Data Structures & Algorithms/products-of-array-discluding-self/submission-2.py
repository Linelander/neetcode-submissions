class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1] * len(nums)
        back = [1] * len(nums)
        back[-1] = nums[-1]
        front[0] = nums[0]

        f = 1
        b = len(nums) - 2
        while f < len(nums) and b >= 0:
            front[f] = front[f-1] * nums[f]
            back[b] = back[b+1] * nums[b]
            f += 1
            b -= 1
        
        result = [0] * len(nums)
        for i in range(len(result)):
            l, r = 1, 1
            if i > 0:
                l = front[i - 1]
            if i < len(nums)-1:
                r = back[i + 1]
            result[i] = l*r
        return result