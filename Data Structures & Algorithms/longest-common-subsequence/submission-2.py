class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0] * (len(text2) + 1)
        corner = 0
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) - 1, -1 , -1):
                temp = row[j]
                row[j] = max(row[j + 1], row[j])
                if text2[j] == text1[i]:
                    row[j] = 1 + corner
                corner = temp
            corner = 0
        return row[0]