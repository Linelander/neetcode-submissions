class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = -1
        resStr = ""
        
        for i in range(len(s)):
            l = i
            r = i
            while (l-1 >= 0 and r+1 < len(s)
                and s[l-1] == s[r+1]):
                l -= 1
                r += 1

            if (r-l+1 > resLen):
                resStr = s[l:r+1]
                resLen = max(resLen, r-l+1)

        for i in range(len(s)):
            print("hey")
            l = i
            r = i+1

            if l >= 0 and r < len(s) and s[l] != s[r]:
                continue

            while (l-1 >= 0 and r+1 < len(s)
                and s[l-1] == s[r+1]):
                l -= 1
                r += 1
                print(r-l+1)

            if (r-l+1 > resLen):
                resStr = s[l:r+1]
                resLen = max(resLen, r-l+1)

        return resStr
