class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)
        mid = (l + r) // 2
        while l <= r:
            if mid == 0 or mid == len(intervals):
                if mid == 0 and r == 1:
                    if intervals[0][0] < newInterval[0]:
                        mid = 1
                break
            if newInterval[0] >= intervals[mid - 1][0] and newInterval[0] <= intervals[mid][0]:
                break
            elif newInterval[0] < intervals[mid - 1][0]:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        minimum = newInterval[0]
        maximum = newInterval[1]
        l = mid
        print(f"mid: {mid}")
        if mid != 0 and intervals[mid - 1][1] >= minimum:
            print("here")
            l = mid - 1
            minimum = intervals[mid - 1][0]
        while mid < len(intervals):
            if intervals[mid][0] <= maximum:
                # print("here1")
                mid += 1
            else:
                break
        if mid != 0:
            maximum = max(maximum, intervals[mid - 1][1])
        # print(intervals[:l])
        # print(f"min max: {[minimum, maximum]}")
        # print(intervals[mid:])
        temp1 = intervals[:l]
        temp1.append([minimum, maximum])
        temp2 = intervals[mid:]
        # print(temp1)
        res = temp1 + temp2
        # print(res)
        return res
