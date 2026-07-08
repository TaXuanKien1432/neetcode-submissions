class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)

        min_heap = []

        for i in range(len(self.nums)):
            if i < self.k:
                heapq.heappush(min_heap, self.nums[i])
            else:
                heapq.heappushpop(min_heap, self.nums[i])
        
        return min_heap[0]

