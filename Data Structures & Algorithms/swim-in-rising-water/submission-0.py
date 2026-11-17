class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], (0, 0))] # list of (t, (row, col))
        visit = set()
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            row, col = node
            if row == n - 1 and col == n - 1:
                return t
            for newRow, newCol in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
                if newRow in range(n) and newCol in range(n) and (newRow, newCol) not in visit:
                    newT = max(t, grid[newRow][newCol])
                    heapq.heappush(minHeap, (newT, (newRow, newCol)))

