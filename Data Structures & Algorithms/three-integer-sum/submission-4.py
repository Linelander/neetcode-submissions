class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        snums = sorted(nums)

        for i in range(len(snums)):
            if i > 0 and snums[i] == snums[i-1]: continue
            target = -snums[i]
            l = i + 1
            if l == len(snums): break
            r = len(snums) - 1

            while l < r:
                sum = snums[l] + snums[r]
                if sum == target:
                    triplets.append([-target, snums[l], snums[r]])
                    r -= 1
                    l += 1
                    while l < r and snums[l] == snums[l-1]: l += 1  # skip duplicates
                    while l < r and snums[r] == snums[r+1]: r -= 1  # skip duplicates

                elif sum > target:
                    r -= 1
                elif sum < target:
                    l += 1

            # if l < r and snums[l] + snums[r] == target:
            #     triplets.append([-target, snums[l], snums[r]])

        return triplets
