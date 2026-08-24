class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        
        cols = set()
        positiveDiagonals = set()
        negativeDiagonals = set()

        def dfs(row):
            if row >= n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                if (
                    col not in cols
                    and row + col not in positiveDiagonals
                    and row - col not in negativeDiagonals
                ):
                    board[row][col] = 'Q'
                    cols.add(col)
                    positiveDiagonals.add(row + col)
                    negativeDiagonals.add(row - col)
                    
                    dfs(row + 1)
                    
                    board[row][col] = '.'
                    cols.remove(col)
                    positiveDiagonals.remove(row + col)
                    negativeDiagonals.remove(row - col)

        dfs(0)
        return res
        