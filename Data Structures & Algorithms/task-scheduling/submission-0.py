class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        heap = [[value, key] for key, value in counts.items()]
        heapq.heapify_max(heap)
        res = 0
        cooling = deque()
        while len(heap) > 0 or len(cooling) > 0:
            res += 1
            if cooling and cooling[0][0] == res:
                heapq.heappush_max(heap, cooling.popleft()[1])
            if len(heap) > 0:
                temp = heapq.heappop_max(heap)
                if temp[0] > 1:
                    # add to queue
                    temp[0] -= 1
                    cooling.append([1 + n + res, temp])
        return res