class Solution:
    def checkValidString(self, s: str) -> bool:
        leftop = 0
        rightop = 0
        total = 0
        for l in s:
            if l == '(':
                total += 1
            elif l == ')':
                if total > 0:
                    total -= 1
                    rightop = min(total, rightop)
                else:
                    if leftop > 0:
                        leftop -= 1
                    else:
                        return False
            else:
                leftop += 1
                if rightop != total:
                    rightop += 1
        if total - rightop == 0:
            return True
        return False