class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord("a")] == None:
                curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord("a")] == None:
                return False
            curr = curr.children[ord(char) - ord("a")]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if curr.children[ord(char) - ord("a")] == None:
                return False
            curr = curr.children[ord(char) - ord("a")]
        return True
        