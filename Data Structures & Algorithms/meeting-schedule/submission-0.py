"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = [[x.start, x.end] for x in intervals]
        heapq.heapify(heap)
        prev = 0
        while len(heap) > 0:
            cur = heapq.heappop(heap)
            if cur[0] < prev:
                return False
            prev = cur[1]
        return True