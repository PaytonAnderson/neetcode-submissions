class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mheap = stones
        heapq.heapify_max(mheap)
        while len(mheap) > 1:
            l = heapq.heappop_max(mheap)
            r = heapq.heappop_max(mheap)
            if l != r:
                heapq.heappush_max(mheap, l - r)
        if len(mheap) == 1:
            return mheap[0]
        return 0