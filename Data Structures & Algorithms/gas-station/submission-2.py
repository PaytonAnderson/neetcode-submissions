class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = gas[0] - cost[0]
        loop = 0
        i = 1
        while i != start and len(gas) != 1:
            cur = gas[i] - cost[i]
            if total < 0:
                if loop == 1:
                    return -1
                start = i
                total = cur
            else:
                total += cur
            i += 1
            if i == len(gas):
                i = 0
                loop = 1
        if total >= 0:
            return start
        return -1