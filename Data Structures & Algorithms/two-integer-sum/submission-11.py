class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen.keys() and seen[difference] != i:
                return [seen[difference], i]
            seen[nums[i]] = i