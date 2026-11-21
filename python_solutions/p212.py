
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):

            ch = board[r][c]
            node = parent.children[ch]

            # Word found
            if node.word is not None:
                result.append(node.word)
                node.word = None

            # Mark visited
            board[r][c] = '#'

            # Explore four directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                    and board[nr][nc] in node.children):

                    dfs(nr, nc, node)

            # Restore board
            board[r][c] = ch

            # Remove exhausted Trie branch
            if not node.children and node.word is None:
                del parent.children[ch]

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
