"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        inter = [[x.start, x.end] for x in intervals]
        days = []
        heapq.heapify(days)
        heapq.heapify(inter)
        while len(inter) > 0:
            if len(days) != 0 and days[0] <= inter[0][0]:
                heapq.heappop(days)
            heapq.heappush(days, heapq.heappop(inter)[1])
        return len(days)