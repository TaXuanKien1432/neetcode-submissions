class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # max heap
        self.largeHeap = [] # min heap

    def addNum(self, num: int) -> None:
        maxInSmallHeap = -1 * self.smallHeap[0] if self.smallHeap else float("-infinity")
        minInLargeHeap = self.largeHeap[0] if self.largeHeap else float("infinity")

        # decide which heap to insert, values in smallHeap < values in largeHeap guaranteed
        if num <= maxInSmallHeap or (num > maxInSmallHeap and num <= minInLargeHeap):
            heapq.heappush(self.smallHeap, -1 * num)
        else:
            heapq.heappush(self.largeHeap, num)
        
        # balance length of the heaps
        if len(self.smallHeap) > 1 + len(self.largeHeap):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.largeHeap) > 1 + len(self.smallHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)

    def findMedian(self) -> float:
        totalLen = len(self.smallHeap) + len(self.largeHeap)

        if totalLen % 2 == 0:
            return (-1 * self.smallHeap[0] + self.largeHeap[0])/2
        else:
            return -1 * self.smallHeap[0] if len(self.smallHeap) > len(self.largeHeap) else self.largeHeap[0]
        