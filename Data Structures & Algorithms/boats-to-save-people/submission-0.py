class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s = sorted(people)
        l = 0
        r = len(s) - 1
        boats = 0
        while l <= r:
            if s[l] + s[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats