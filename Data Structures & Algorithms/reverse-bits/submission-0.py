from collections import deque

class Solution:
    def reverseBits(self, n: int) -> int:
        queue = deque()
        for i in range(0, 32):
            queue.append(1 & n)
            n = n >> 1
        x = 0
        while queue:
            x = x << 1
            x = x | queue.popleft()
        return x