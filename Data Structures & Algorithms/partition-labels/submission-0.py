class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexes = {}
        for i in range(len(s)): 
            temp = indexes.get(s[i], [i, i])
            temp[1] = i
            indexes[s[i]] = temp
        idxheap = list(indexes.values())
        heapq.heapify(idxheap)
        res = []
        i = 0
        while len(idxheap) > 0:
            cur = heapq.heappop(idxheap)
            start = cur[0]
            end = cur[1]
            while len(idxheap) > 0 and idxheap[0][0] < end:
                temp = heapq.heappop(idxheap)
                end = max(end, temp[1])
            i = end + 1
            res.append(end - start + 1)
        return res
