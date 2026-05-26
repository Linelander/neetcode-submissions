class Solution:
    def countBits(self, n: int) -> List[int]:
        
        cache = [-1] * (n+1)
        def setBits(i):
            if cache[i >> 1] != -1:
                cache[i] = cache[i >> 1] + (i & 1)
                return cache[i >> 1] + (i & 1)
            cache[i] = (i & 1)
            return cache[i]

        result = []
        for i in range(0, n+1):
            result.append(setBits(i))
        
        return result