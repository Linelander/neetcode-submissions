class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1
            while 2 in counts.values():
                counts[s[l]] += -1
                l += 1
            longest = max(longest, r - l + 1)

        return longest