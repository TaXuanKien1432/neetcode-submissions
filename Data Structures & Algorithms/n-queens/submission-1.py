class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = []
        board = [['.' for i in range(n)] for j in range(n)]

        def dfs(row, col):
            if row >= n:
                res.append(curr.copy())
                return
            if (
                not self.leftDiagonal(board, row, col)
                and not self.upVertical(board, row, col)
                and not self.rightDiagonal(board, row, col, n)
            ):
                board[row][col] = 'Q'
                curr.append(self.currentPlacement(board, row))
                if row + 1 < n:
                    for nextCol in range(n):
                        dfs(row + 1, nextCol)
                else:
                    dfs(row + 1, 0)
                board[row][col] = '.'
                curr.pop()

        for col in range(n):
            dfs(0, col)
        return res

    def leftDiagonal(self, board, row, col):
        while row - 1 >= 0 and col - 1 >= 0:
            row, col = row - 1, col - 1
            if board[row][col] == 'Q':
                return True
        return False

    def rightDiagonal(self, board, row, col, n):
        while row - 1 >= 0 and col + 1 < n:
            row, col = row - 1, col + 1
            if board[row][col] == 'Q':
                return True
        return False

    def upVertical(self, board, row, col):
        while row - 1 >= 0:
            row -= 1
            if board[row][col] == 'Q':
                return True
        return False
            
    def currentPlacement(self, board, row):
        currentPlacement = ''
        for col in board[row]:
            currentPlacement += col
        return currentPlacement


    

