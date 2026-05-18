class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        validSell = 0
        lastSell = 0
        lastBuy = float('-inf')
        for i in range(n):
            tempBuy = max(lastBuy, validSell - prices[i])
            validSell = lastSell
            lastSell = max(lastBuy + prices[i], lastSell)
            lastBuy = tempBuy
        return lastSell