class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        row = [False] * (len(s1) + 1)
        for i in range(1 + len(s2)):
            for j in range((len(s1) + 1)):
                if i == 0 and j == 0:
                    row[j] = True 
                elif i > 0 and row[j] and s3[i + j - 1] == s2[i - 1]:
                    row[j] = True
                elif j > 0 and row[j - 1] and s3[i + j -1] == s1[j- 1]:
                    row[j] = True
                else:
                    row[j] = False
        return row[-1]