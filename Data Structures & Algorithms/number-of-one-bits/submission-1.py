class Solution:
    def hammingWeight(self, n: int) -> int:
        "xor each bit with 1, if changes add one to total"
        w = 0
        b = 1
        prev = n
        while n != 0:
            print(n)
            n ^= b
            if n < prev:
                w += 1
                prev = n
            else:
                n = prev
            b *= 2
        return w
