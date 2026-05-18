class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums) - 1:
            # print(f"\ni: {i}\n")
            if count == 10:
                return -1
            count += 1
            cur = i + nums[i]
            print(cur)
            if cur >= len(nums) - 1:
                return count
            m = cur
            index = cur
            for j in range(1, nums[i] + 1):
                # print(f"m:{m}")
                # print(f"i + j + nums[j]: {i + j + nums[j]}")
                if cur + nums[j] >= m:
                    m = i + j + nums[j]
                    index = i + j
            i = index
            # print(f"count: {count} cur: {cur} m: {m} i: {i}")
        return count 