class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        while counts:
            start = min(counts.keys())
            for i in range(groupSize):
                if not counts:
                    return False
                cur = counts.get(start + i, 0)
                if cur == 0:
                    return False
                if cur == 1:
                    del counts[start + i]
                else:
                    counts[start + i] = cur - 1
        return True