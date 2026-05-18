class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            new = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                new += digit * digit
            n = new
        return True

        