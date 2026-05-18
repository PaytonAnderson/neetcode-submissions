class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur = prices[0]
        for price in prices:
            if cur < price:
                profit += price - cur
                cur = price
            else:
                cur = price
        return profit