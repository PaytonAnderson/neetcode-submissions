class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        row = [1] * (len(s) + 1)
        for i in range(len(t)):
            newRow = [0] * (len(s) + 1)
            for j in range(i + 1, len(s) + 1):
                if s[j - 1] == t[i]:
                    newRow[j] = row[j - 1] + newRow[j - 1]
                else:
                    newRow[j] = newRow[j - 1]
            row = newRow
        return newRow[-1]