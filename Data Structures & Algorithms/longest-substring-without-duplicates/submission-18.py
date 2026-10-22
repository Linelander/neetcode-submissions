class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counts = defaultdict(int)

        mp = {}

        # revisiting in october and taking notes

        for r in range(len(s)):         # starting window from the left
            counts[s[r]] += 1           # counting as we go. in sliding window one side should always move
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)   # check for new best

        # but it's too slow?

        return longest