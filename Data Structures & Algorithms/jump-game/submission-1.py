class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)
        def dfs(index):
            if index >= len(nums) - 1:
                return True
            if visited[index] == True:
                return False
            visited[index] = True
            i = nums[index]
            while i > 0:
                if dfs(index + i) == True:
                    return True
                i -= 1
            return False
        return dfs(0)
        