class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret += '!'
            ret += s
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        strs = []
        while len(s) > 0:
            i = 0
            while s[i] != '!':
                i += 1
            l = int(s[0:i])
            strs.append(s[i+1:i+1+l])
            s = s[l+i+1:]
        return strs

