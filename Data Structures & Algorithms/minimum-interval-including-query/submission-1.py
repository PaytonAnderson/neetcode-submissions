class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [[x[0], x[1], x[1] - x[0] + 1] for x in intervals]
        heapq.heapify(intervals)
        queries = [[queries[i], i] for i in range(len(queries))]
        queries = sorted(queries)
        prev = 0
        prevSize = -1
        res = [None] * len(queries)
        for q in queries:
            if q[0] == prev:
                res[q[1]] = prevSize
                continue
            prev = q[0]
            size = float('inf')
            while len(intervals) > 0 and intervals[0][0] <= q[0]:
                temp = heapq.heappop(intervals)
                if temp[1] >= q[0]:
                    size = min(size, temp[2])
                    if temp[1] > q[0]:
                        heapq.heappush(intervals, [q[0] + 1, temp[1], temp[2]])
            if size == float('inf'):
                size = -1
            prevSize = size
            res[q[1]] = size
        return res