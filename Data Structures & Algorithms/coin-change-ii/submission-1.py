class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prevRow = [0] * (amount + 1)
        curRow = [0] * (amount + 1)
        curRow[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    curRow[i] = curRow[i - coin] + prevRow[i]
                else:
                    curRow[i] = prevRow[i]
            prevRow = curRow
        return curRow[amount]