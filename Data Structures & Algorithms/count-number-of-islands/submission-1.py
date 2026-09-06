class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = [0]
        rows, cols = len(grid), len(grid[0])
        
        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            grid[row][col] = '#'

            while queue:
                row, col = queue.popleft()

                if row - 1 >= 0 and grid[row - 1][col] == '1':
                    queue.append((row - 1, col))
                    grid[row - 1][col] = '#'

                if row + 1 < rows and grid[row + 1][col] == '1':
                    queue.append((row + 1, col))
                    grid[row + 1][col] = '#'

                if col - 1 >= 0 and grid[row][col - 1] == '1':
                    queue.append((row, col - 1))
                    grid[row][col - 1] = '#'

                if col + 1 < cols and grid[row][col + 1] == '1':
                    queue.append((row, col + 1))
                    grid[row][col + 1] = '#'

            res[0] += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row, col)

        return res[0]
                
