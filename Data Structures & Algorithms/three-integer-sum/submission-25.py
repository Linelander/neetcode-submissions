class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        result = []

        print(snums)

        i = 0
        while i < len(snums):
            l, r = i+1, len(snums) - 1
            while l < r:
                threesum = snums[i] + snums[l] + snums[r]
                if threesum == 0:
                    result.append([snums[i], snums[l], snums[r]])

                if threesum >= 0:
                    oldr = snums[r]
                    while r > l and snums[r] == oldr:
                        r -= 1
                else:
                    oldl = snums[l]
                    while l < r and snums[l] == oldl:
                        l += 1

            oldi = snums[i]
            while i < len(snums) and snums[i] == oldi:
                i += 1

        return result
                
                
