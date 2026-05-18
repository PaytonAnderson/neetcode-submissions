class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = nums[0]
        for num in nums[1:]:
            cur += num
            cur = max(cur, num)
            best = max(best, cur)
        return best