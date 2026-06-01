import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # stores tuple (frequency, number)
        counter = {} # maps number to frequency

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num, freq in counter.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        return [num for freq, num in heap]