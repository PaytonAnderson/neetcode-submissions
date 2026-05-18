class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        res = []
        for i in intervals[1:]:
            if i[0] > r:
                res.append([l, r])
                l = i[0]
                r = i[1]
            else:
                r = max(r, i[1])
        res.append([l, r])
        return res
