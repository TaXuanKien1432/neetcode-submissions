class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board_rows, board_cols = len(board), len(board[0])
        board_cells = board_rows * board_cols
        res = []
        visited = set() # contains (row, col)
        # create trie that contains all the words
        trie = Trie()
        for word in words:
            curr = trie.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isEnd = True

        # dfs each cell
        def dfs(i, node, currWord, row, col):
            if (
                i == board_cells or
                row < 0 or row >= board_rows or
                col < 0 or col >= board_cols or
                board[row][col] not in node.children
                or (row, col) in visited
            ):
                return
            else:
                char = board[row][col]
                if node.children[char].isEnd:
                    res.append(currWord + char)
                    node.children[char].isEnd = False
                visited.add((row, col))
                dfs(i + 1, node.children[char], currWord + char, row, col - 1)
                dfs(i + 1, node.children[char], currWord + char, row - 1, col)
                dfs(i + 1, node.children[char], currWord + char, row, col + 1)
                dfs(i + 1, node.children[char], currWord + char, row + 1, col)
                visited.remove((row, col))

        for r in range(board_rows):
            for c in range(board_cols):
                dfs(0, trie.root, "", r, c)

        return res
                

        