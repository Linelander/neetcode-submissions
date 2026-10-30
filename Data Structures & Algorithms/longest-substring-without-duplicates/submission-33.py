class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = {}
        longest = 0

        for r in range(len(s)):
            new = s[r]
            if new in seen:
                l = max(seen[new] + 1, l) # remove last seen, move up only
            seen[new] = r
            longest = max((r - l) + 1, longest)

        return longest
            
