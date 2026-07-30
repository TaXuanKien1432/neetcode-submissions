class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numOfRows, numOfColumns = len(board), len(board[0])
        
        def dfs(row, column, curr, visited, word):
            if curr == word:
                return True
            if len(curr) > len(word) or curr[len(curr) - 1] != word[len(curr) - 1]:
                return False

            up = False
            if row > 0 and (row - 1, column) not in visited:
                visited.add((row - 1, column))
                up = dfs(row - 1, column, curr + board[row - 1][column], visited, word)
                visited.remove((row - 1, column))
            
            down = False
            if row < numOfRows - 1 and (row + 1, column) not in visited:
                visited.add((row + 1, column))
                down = dfs(row + 1, column, curr + board[row + 1][column], visited, word)
                visited.remove((row + 1, column))
            
            left = False
            if column > 0 and (row, column - 1) not in visited:
                visited.add((row, column - 1))
                left = dfs(row, column - 1, curr + board[row][column - 1], visited, word)
                visited.remove((row, column - 1))

            right = False
            if column < numOfColumns - 1 and (row, column + 1) not in visited:
                visited.add((row, column + 1))
                right = dfs(row, column + 1, curr + board[row][column + 1], visited, word)
                visited.remove((row, column + 1))
            
            return up or down or left or right
        
        for row in range(numOfRows):
            for column in range(numOfColumns):
                if dfs(row, column, board[row][column], {(row, column)}, word):
                    return True
        
        return False