class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for start, end, weight in flights:
            adj[start].append((end, weight))
        
        H = k + 1
        minH = [(0, src, 0)] # (distance, node, h)
        stops = [float("inf")] * n

        while minH:
            distance, node, h = heapq.heappop(minH)
            if node == dst:
                return distance
            if h >= stops[node] or h == H:
                continue
            stops[node] = h
            for nei, dis in adj[node]:
                heapq.heappush(minH, (distance + dis, nei, h + 1))
        
        return -1
            