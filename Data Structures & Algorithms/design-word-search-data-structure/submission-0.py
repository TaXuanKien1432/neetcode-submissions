class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.word
            
            if word[i] == '.':
                for childNode in node.children.values():
                    if dfs(i + 1, childNode):
                        return True
            else:
                if word[i] not in node.children:
                    return False
                return dfs(i + 1, node.children[word[i]])
            return False
        return dfs(0, self.root)
