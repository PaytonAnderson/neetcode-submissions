class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ret = []
        s = {}
        for num in nums:
            if num in s:
                s[num] += 1
                if s[num] == 1 + (len(nums) // 3):
                    ret.append(num)
                    if len(ret) == 2:
                        return ret
            else:
                s[num] = 1
                if len(nums) < 3:
                    ret.append(num)
        return ret