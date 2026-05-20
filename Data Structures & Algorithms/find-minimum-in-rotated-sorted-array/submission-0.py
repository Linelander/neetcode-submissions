class Solution:
    def findMin(self, nums: List[int]) -> int:
        shifts = 0
        last = float('-inf')
        for num in nums:
            if num < last: break
            last = num
            shifts += 1

        # print(shifts)

        # find the number of shifts
        
        # for i in range(len(nums)):
        #     index = ((i + (shifts)) % len(nums)) # correct
        #     print(nums[index])


        
        return nums[((0 + (shifts)) % len(nums))] # correct


    # 0 % 6 = 0


        