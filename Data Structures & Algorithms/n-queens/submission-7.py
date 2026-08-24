class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = []
        cols = set()
        positiveDiagonals = set()
        negativeDiagonals = set()
        board = [['.' for i in range(n)] for j in range(n)]

        def dfs(row):
            if row >= n:
                res.append(curr.copy())
                return
            for col in range(n):
                if (
                    col not in cols
                    and row + col not in positiveDiagonals
                    and row - col not in negativeDiagonals
                ):
                    board[row][col] = 'Q'
                    curr.append(self.currentPlacement(board, row))
                    cols.add(col)
                    positiveDiagonals.add(row + col)
                    negativeDiagonals.add(row - col)
                    dfs(row + 1)
                    board[row][col] = '.'
                    curr.pop()
                    cols.remove(col)
                    positiveDiagonals.remove(row + col)
                    negativeDiagonals.remove(row - col)

        dfs(0)
        return res
            
    def currentPlacement(self, board, row):
        currentPlacement = ''
        for col in board[row]:
            currentPlacement += col
        return currentPlacement
        