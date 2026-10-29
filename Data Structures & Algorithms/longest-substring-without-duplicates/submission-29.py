class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1) # s[r] could be back before l. don't want that
            seen[s[r]] = r # update location where s[r] last seen
            longest = max(longest, (r-l) + 1)

        return longest