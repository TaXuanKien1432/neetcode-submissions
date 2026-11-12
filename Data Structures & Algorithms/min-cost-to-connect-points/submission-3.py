class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))

        minH = [(0, 0)]
        visited = set()
        cost = 0

        while minH:
            distance, i = heapq.heappop(minH)
            if i in visited:
                continue
            visited.add(i)
            cost += distance
            for distanceJ, j in adj[i]:
                if j not in visited:
                    heapq.heappush(minH, (distanceJ, j))
        
        return cost

