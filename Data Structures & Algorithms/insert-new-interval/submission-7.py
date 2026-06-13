class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            i += 1
        print(i)
        intervals.insert(i, newInterval)
        print(intervals)

        x = 1
        while x < len(intervals):
            if intervals[x][0] <= intervals[x-1][1]:
                intervals[x-1][1] = max(intervals[x-1][1], intervals[x][1])
                del intervals[x]
            else:
                x += 1

        return intervals