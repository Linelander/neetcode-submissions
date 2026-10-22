class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0

        seen = {}

        # revisiting in october and taking notes

        for r in range(len(s)):         # starting window from the left
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
                    # this skips past the leftmost previous version of the letter
                    # but when would l be >?
                    # answer: need it so we don't jump back and get abba -> "bba"
                # l = seen[s[r]] + 1
                # l = r

                # why is max needed here?
            seen[s[r]] = r
            # print(r - l + 1)
            longest = max(longest, r - l + 1)   # check for new best

        # but it's too slow?

        return longest