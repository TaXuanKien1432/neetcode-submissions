import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # stores tuple (frequency, number)
        counter = {} # maps number to frequency

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num in counter.keys():
            if len(heap) >= k:
                heapq.heappushpop(heap, (counter[num], num))
            else:
                heapq.heappush(heap, (counter[num], num))
        
        return [tup[1] for tup in heap]