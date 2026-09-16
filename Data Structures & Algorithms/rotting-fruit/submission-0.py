class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            ans += 1

        return ans if fresh == 0 else -1