class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return math.sqrt(point[0] * point[0] + point[1] * point[1])

        ans = []
        minHeap = []
        store = collections.defaultdict(list)

        for i in range(len(points)):
            minusDistance = -distance(points[i])
            store[minusDistance].append(points[i])

            if i < k:
                heapq.heappush(minHeap, minusDistance)
            else:
                heapq.heappushpop(minHeap, minusDistance)

        for minusDistance in minHeap:
            for i in range(len(store[minusDistance])):
                ans.append(store[minusDistance][i])
            del store[minusDistance]

        return ans

