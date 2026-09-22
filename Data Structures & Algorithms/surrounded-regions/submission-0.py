class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurrounded = set()
        rows, cols = len(board), len(board[0])
        q = collections.deque()

        # Append all 'O' edges into the queue

        for c in range(0, cols - 1):
            if board[0][c] == 'O':
                q.append((0, c))
                notSurrounded.add((0, c))
        
        for r in range(0, rows - 1):
            if board[r][cols - 1] == 'O':
                q.append((r, cols - 1))
                notSurrounded.add((r, cols - 1))

        for c in range(1, cols):
            if board[rows - 1][c] == 'O':
                q.append((rows - 1, c))
                notSurrounded.add((rows - 1, c))

        for r in range(1, rows):
            if board[r][0] == 'O':
                q.append((r, 0))
                notSurrounded.add((r, 0))

        # multi source BFS
        while q:
            r, c = q.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr in range(rows) and nc in range(cols)
                and (nr, nc) not in notSurrounded and board[nr][nc] == 'O'):
                    q.append((nr, nc))
                    notSurrounded.add((nr, nc))

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == 'O' and (r, c) not in notSurrounded:
                    board[r][c] = 'X'




