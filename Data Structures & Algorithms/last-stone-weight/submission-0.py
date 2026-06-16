class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        print(stones)
        while len(stones) > 1:
            biggest = stones.pop(len(stones) - 1)
            print("biggest: ", biggest)
            print("second biggest: ", stones[len(stones) - 1])
            stones[len(stones) - 1] = biggest - stones[len(stones) - 1]
            print("stones: ", stones)
            stones = sorted(stones)
        return stones[0]