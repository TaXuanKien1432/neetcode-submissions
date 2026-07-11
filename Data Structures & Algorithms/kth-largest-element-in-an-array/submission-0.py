class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappushpop(minHeap, nums[i])
            
        return minHeap[0]