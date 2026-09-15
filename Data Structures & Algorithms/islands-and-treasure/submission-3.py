class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != inf):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 1 + grid[r][c]

