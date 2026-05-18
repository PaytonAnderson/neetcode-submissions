class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        l = self.sortArray(nums[0:len(nums)//2])
        r = self.sortArray(nums[len(nums)//2: len(nums)])
        sl = len(l)
        sr = len(r)
        curl = 0
        curr = 0
        ret = []
        while curl < sl and curr < sr:
            if l[curl] < r[curr]:
                ret.append(l[curl])
                curl += 1
            else:
                ret.append(r[curr])
                curr += 1
        while curl < sl:
            ret.append(l[curl])
            curl +=1
        while curr < sr:
            ret.append(r[curr])
            curr +=1
        return ret
            
