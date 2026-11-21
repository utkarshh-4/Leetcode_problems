class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if node.children[index] is None:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.isEnd = True

    def search(self, word: str) -> bool:

        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if node.children[index] is None:
                return False

            node = node.children[index]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            index = ord(ch) - ord('a')

            if node.children[index] is None:
                return False

            node = node.children[index]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)