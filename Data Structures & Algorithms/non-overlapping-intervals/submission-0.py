class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        right = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if i[0] < right:
                res += 1
                right = min(right, i[1])
            else:
                right = i[1]
        return res