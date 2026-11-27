class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        running = 0
        total = 0

        for n in nums:
            running += n
            total += seen[running - k]
            seen[running] += 1

        return total