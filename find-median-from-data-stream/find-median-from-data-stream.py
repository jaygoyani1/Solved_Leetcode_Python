from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heappush(self.hi,-heappushpop(self.lo,-num))
        else:
            heappush(self.lo,-heappushpop(self.hi,num))

    def findMedian(self) -> float:
        return float(self.hi[0]-self.lo[0])/2.0 if len(self.lo) == len(self.hi) else float(self.hi[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()