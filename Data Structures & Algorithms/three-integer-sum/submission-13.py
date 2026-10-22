class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # go through the list
        # and then look for pairs that sum to 0 with it?

        # don't need to check the left

        # can put a pointer at the beginning and end of the remaining 
        # list and move each pointer inward to make it
        # bigger / smaller 

        result = []
        snums = sorted(nums)
        
        i = 0
        while i < len(snums):
            target = snums[i]
            l = i+1
            r = len(snums) - 1
            while l < r:
                cancel = snums[l] + snums[r]
                if target + cancel == 0:
                    result.append([snums[i], snums[l], snums[r]])
                if cancel + target < 0:
                    oldl = snums[l]
                    while snums[l] == oldl and l < r:
                        l += 1
                else: 
                    oldr = snums[r]
                    while snums[r] == oldr and r >= l:
                        r -= 1
            oldi = snums[i]
            while i < len(snums) and snums[i] == oldi:
                i += 1

        
        return result