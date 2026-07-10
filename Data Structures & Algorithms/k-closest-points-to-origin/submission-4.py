class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return math.sqrt(point[0] * point[0] + point[1] * point[1])

        minHeap = []

        for i in range(len(points)):
            minusDistance = -distance(points[i])
            x = points[i][0]
            y = points[i][1]

            if i < k:
                heapq.heappush(minHeap, [minusDistance, x, y])
            else:
                heapq.heappushpop(minHeap, [minusDistance, x, y])

        return [[x, y] for minusDistance, x, y in minHeap]

