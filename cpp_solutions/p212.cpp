
class Solution {
    struct TrieNode {
        TrieNode* children[26] = {};
        string word = "";
    };

    TrieNode* root = new TrieNode();
    vector<string> result;

    void dfs(vector<vector<char>>& board, int r, int c,
             TrieNode* parent) {

        char ch = board[r][c];
        TrieNode* node = parent->children[ch - 'a'];

        if (node->word != "") {
            result.push_back(node->word);
            node->word = "";
        }

        board[r][c] = '#';

        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < board.size() &&
                nc >= 0 && nc < board[0].size() &&
                board[nr][nc] != '#' &&
                node->children[board[nr][nc] - 'a']) {

                dfs(board, nr, nc, node);
            }
        }

        board[r][c] = ch;

        if (node->word == "") {
            bool empty = true;

            for (int i = 0; i < 26; i++) {
                if (node->children[i]) {
                    empty = false;
                    break;
                }
            }

            if (empty) {
                delete node;
                parent->children[ch - 'a'] = nullptr;
            }
        }
    }

public:
    vector<string> findWords(vector<vector<char>>& board,
                             vector<string>& words) {

        for (string& word : words) {
            TrieNode* node = root;

            for (char ch : word) {
                int index = ch - 'a';

                if (!node->children[index])
                    node->children[index] = new TrieNode();

                node = node->children[index];
            }

            node->word = word;
        }

        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (root->children[board[r][c] - 'a']) {
                    dfs(board, r, c, root);
                }
            }
        }

        return result;
    }
};
