class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        split = 0
        while l < r:
            if s[l] != s[r]:
                if split == -1:
                    return False
                elif split == 0:
                    l += 1
                    split = l
                else:
                    l = split - 1
                    r = len(s) - split - 1
                    split = -1
            else:
                l += 1
                r -= 1
        return True