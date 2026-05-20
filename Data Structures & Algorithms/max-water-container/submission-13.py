class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maximum = 0;

        while l < r:            
            maximum = max(maximum, min(heights[l], heights[r]) * (r - l)) # volume
            if (heights[l] < heights[r]): l += 1
            else: r -= 1 # feels arbitrary

        return maximum