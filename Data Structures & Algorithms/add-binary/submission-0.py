class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        m = max(len(a), len(b))
        for i in range(m):
            if len(a) - 1 -i < 0:
                cur = "0"
            else:
                cur = a[len(a) - 1 -i]
            if len(b) - 1 - i < 0:
                cur2 = "0"
            else:
                cur2 = b[len(b) - 1 - i]
            if cur == "1" and cur2 == "1":
                if carry == 1:
                    res = "1" + res
                else:
                    res = "0" + res
                carry = 1
            elif (cur == "1" and cur2 == "0") or (cur == "0" and cur2 == "1"):
                if carry == 1:
                    res = "0" + res
                    carry = 1
                else:
                    res = "1" + res
                    carry = 0
            else:
                if carry == 1:
                    res = "1" + res
                else:
                    res = "0" + res
                carry = 0
        if carry == 1:
            return "1" + res
        return res