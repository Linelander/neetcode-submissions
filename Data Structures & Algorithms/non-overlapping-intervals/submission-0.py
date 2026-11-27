class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]
        removals = 0

        for start, end in intervals[1:]:
            if start >= prevEnd:    # no overlap. move end
                prevEnd = end
            else:                       # overlap
                removals += 1       # remove the one with the larger end
                prevEnd = min(prevEnd, end)

        return removals