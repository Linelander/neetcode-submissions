from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        for r in range(len(s2)):
            # add arr[r] to window state          # 1. expand right
            window = s2[l:r + 1]

            if r - l + 1 == len(s1):         # 2. window is full
                # check / record answer            # 3. evaluate this window
                if Counter(window) == Counter(s1):
                    return True
                l += 1                           #    slide forward

        return False