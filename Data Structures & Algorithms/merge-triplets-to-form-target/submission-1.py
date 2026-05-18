class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        prev = [0, 0, 0]
        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                prev[0] = max(prev[0], trip[0])
                prev[1] = max(prev[1], trip[1])
                prev[2] = max(prev[2], trip[2])
            if prev == target:
                return True
        return False