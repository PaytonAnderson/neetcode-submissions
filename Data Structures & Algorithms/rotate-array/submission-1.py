class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = nums[0]
        start = 0
        cur = k % len(nums)
        count = 0
        while count < len(nums):
            if cur == start and count != 0:
                nums[start] = prev
                start += 1
                prev = nums[start]
                cur += 1 + k
                cur = cur % len(nums)
                count += 1
                if count == len(nums):
                    return
            temp = nums[cur]
            nums[cur] = prev
            prev = temp
            cur += k
            cur = cur % len(nums)
            count += 1
        return 
        