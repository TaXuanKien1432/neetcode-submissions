class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])

        # add cells that can flow water to pacific
        pacificQueue = collections.deque()
        for c in range(cols):
            pacificQueue.append([0, c])
            pacific.add((0, c))

        for r in range(1, rows):
            pacificQueue.append([r, 0])
            pacific.add((r, 0))

        while pacificQueue:
            r, c = pacificQueue.popleft()
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if (nr in range(rows) and nc in range(cols)
                and (nr, nc) not in pacific and heights[nr][nc] >= heights[r][c]):
                    pacificQueue.append([nr, nc])
                    pacific.add((nr, nc))

        # add cells that can flow water to atlantic
        atlanticQueue = collections.deque()
        for c in range(cols):
            atlanticQueue.append([rows - 1, c])
            atlantic.add((rows - 1, c))

        for r in range(rows - 1):
            atlanticQueue.append([r, cols - 1])
            atlantic.add((r, cols - 1))

        while atlanticQueue:
            r, c = atlanticQueue.popleft()
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if (nr in range(rows) and nc in range(cols)
                and (nr, nc) not in atlantic and heights[nr][nc] >= heights[r][c]):
                    atlanticQueue.append([nr, nc])
                    atlantic.add((nr, nc))

        # combine both results 
        return [[r, c] for r, c in pacific & atlantic]

