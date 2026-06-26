from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        print(counts)
        return counts.most_common()[-1][0]