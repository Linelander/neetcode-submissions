class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()

        def bt(state):
            if len(state) == len(nums):
                result.append(state[:])
                return state

            for num in nums:
                if num not in seen:
                    state.append(num)
                    seen.add(num)
                    bt(state)
                    state.pop()
                    seen.remove(num)

        bt([])
        return result