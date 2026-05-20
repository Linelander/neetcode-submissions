from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_freqs = defaultdict(int)
        
        for num in nums:
            d_freqs[num] += 1;

        # sort by frequencies, but only return keys
        # return sorted(list(d_freqs.keys()), reverse=True)[:k]
        return sorted(d_freqs, key=lambda x: d_freqs[x], reverse=True)[:k]
        