class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        candidates = sorted(candidates)

        def bt(start, state):
            if sum(state) == target:
                result.append(state[:])
                return
            if sum(state) > target:
                return

            for i in range(start, len(candidates)):
                # recursive calls will obtain duplicates
                # they're filtered out of the parent
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                state.append(candidates[i])
                bt(i + 1, state)
                state.pop()

        bt(0, [])
        return result