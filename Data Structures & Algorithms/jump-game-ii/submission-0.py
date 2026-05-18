class Solution:
    def jump(self, nums: List[int]) -> int:
        goals = {len(nums) - 1: 0}
        for i in range(len(nums) -1, -1, -1):
            best = float('inf')
            for j in range(nums[i], 0, -1):
                best = min(best, goals.get(i + j, float('inf')))
            if best != float('inf'):
                goals[i] = best + 1
        return goals[0]