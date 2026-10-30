class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        slowest = float('inf')

        # we are searching the RATES not the indexes of piles

        while l <= r:
            t = 0
            k = (l + r) // 2
            for p in piles:
                t += math.ceil(p / k)
            if t <= h:
                slowest = min(slowest, k)
                r = k-1
            else:
                l = k+1 # go faster


        return slowest