class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = []
        board = [['.' for i in range(n)] for j in range(n)]

        def dfs(row):
            if row >= n:
                res.append(curr.copy())
                return
            for col in range(n):
                if (
                    not self.leftDiagonal(board, row, col)
                    and not self.upVertical(board, row, col)
                    and not self.rightDiagonal(board, row, col, n)
                ):
                    board[row][col] = 'Q'
                    curr.append(self.currentPlacement(board, row))
                    dfs(row + 1)
                    board[row][col] = '.'
                    curr.pop()

        dfs(0)
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


    

