class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            nextdp = defaultdict(int)
            for sum, count in dp.items():
                nextdp[sum + num] += count
                nextdp[sum - num] += count
            dp = nextdp
        return dp[target]


