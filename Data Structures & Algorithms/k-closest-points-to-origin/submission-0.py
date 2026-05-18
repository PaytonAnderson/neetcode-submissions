class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i] = (pow(pow(points[i][0], 2) + pow(points[i][1], 2), 1/2), points[i])
        heapq.heapify_max(points)
        while len(points) > k:
            heapq.heappop_max(points)
        points = [x[1] for x in points]
        return points