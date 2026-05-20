class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        counts = defaultdict(int)
        l = 0

        for r in range(len(s)):
            # right crawl
            counts[s[r]] += 1

            # left crawl
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] += -1
                l += 1
            
            result = max(result, r - l + 1)

        return result
