class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for i in range(len(stones)):
            heapq.heappush(maxHeap, stones[i] * -1)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap) * -1
            y = heapq.heappop(maxHeap) * -1

            if x > y:
                heapq.heappush(maxHeap, (x - y) * -1)

        return -1 * maxHeap[0] if len(maxHeap) == 1 else 0
