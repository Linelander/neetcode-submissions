class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key=lambda x: x[0])

        start = 0
        end = 1

        i = 1
        while i < len(intervals):
            prev = intervals[i-1]
            curr = intervals[i]
            if (prev[end] >= curr[start]):
                curr[start] = min(prev[start], curr[start])
                curr[end] = max(prev[end], curr[end])
                del intervals[i-1]
                i -= 1
            i += 1


        # intervals.sort(key=lambda x: x[1])
        # if len(intervals) > 1:
        #     j = len(intervals)-2
        #     while j >= 0:
        #         prev = intervals[j+1]
        #         curr = intervals[j]
        #         if (prev[start] <= curr[end]):
        #             curr[start] = min(prev[start], curr[start])
        #             curr[end] = max(prev[end], curr[end])
        #             del intervals[j-1]
        #         j -= 1

        return intervals
