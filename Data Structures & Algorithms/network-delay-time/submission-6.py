class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for u, v, t in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        minTime = 0
        visit = set()

        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in visit:
                continue
            visit.add(u1)
            minTime = max(minTime, t1)
            for u2, t2 in edges.get(u1, []):
                if u2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, u2))

        return minTime if len(visit) == n else -1

