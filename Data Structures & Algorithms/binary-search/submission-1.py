class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0 #index of target
            else:
                return -1
        if target == nums[len(nums)//2]:
            return len(nums)//2
        if target < nums[len(nums)//2]:
            index =  self.search(nums[:len(nums)//2], target)
            if index == -1:
                return -1
            return index
        else:
            index = self.search(nums[len(nums)//2:], target)
            if index == -1:
                return -1
            return index + len(nums)//2 #adjust index
        