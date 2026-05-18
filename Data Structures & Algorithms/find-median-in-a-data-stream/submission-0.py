class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []
        heapq.heapify_max(self.h1)
        heapq.heapify(self.h2)

    def addNum(self, num: int) -> None:
        if len(self.h1) == 0:
            if len(self.h2) == 0:
                heapq.heappush_max(self.h1, num)
            else:
                if self.h2[0] >= num:
                    heapq.heappush_max(self.h1, num)
                else:
                    heapq.heappush_max(self.h1, heapq.heappop(self.h2))
                    heapq.heappush(self.h2, num)
        elif len(self.h2) == 0:
            if self.h1[0] <= num:
                heapq.heappush(self.h2, num)
            else:
                heapq.heappush(self.h2, heapq.heappop_max(self.h1))
                heapq.heappush_max(self.h1, num)
        else:
            #both heaps have at least one element
            if len(self.h1) == len(self.h2):
                if self.h1[0] >= num:
                    heapq.heappush_max(self.h1, num)
                else:
                    heapq.heappush(self.h2, num)
            elif len(self.h1) > len(self.h2):
                if self.h1[0] <= num:
                    heapq.heappush(self.h2, num)
                else:
                    heapq.heappush(self.h2, heapq.heappop_max(self.h1))
                    heapq.heappush_max(self.h1, num)
            else:
                if self.h2[0] >= num:
                    heapq.heappush_max(self.h1, num)
                else:
                    heapq.heappush_max(self.h1, heapq.heappop(self.h2))
                    heapq.heappush(self.h2, num)

    def findMedian(self) -> float:
        if len(self.h1) > len(self.h2):
            return self.h1[0]
        elif len(self.h2) > len(self.h1):
            return self.h2[0]
        else:
            return (self.h1[0] + self.h2[0]) / 2
        