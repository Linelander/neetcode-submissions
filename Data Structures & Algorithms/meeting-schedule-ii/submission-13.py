"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda m: m.start)
        
        if not intervals: return 0
        rooms = [[intervals.pop(0)]]

        for interval in intervals:
            placed = False
            for room in rooms:
                if room[len(room) - 1].end <= interval.start:
                    room.append(interval)
                    placed = True
                    break
            if not placed:
                rooms.append([interval])

        return len(rooms)