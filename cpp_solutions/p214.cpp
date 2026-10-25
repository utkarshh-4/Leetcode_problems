class Solution {
public:
    string shortestPalindrome(string s) {
        string rev = s;
        reverse(rev.begin(), rev.end());

        string combined = s + "#" + rev;
        int n = combined.size();

        vector<int> lps(n, 0);

        for (int i = 1; i < n; i++) {
            int len = lps[i - 1];

            while (len > 0 && combined[i] != combined[len]) {
                len = lps[len - 1];
            }

            if (combined[i] == combined[len]) {
                len++;
            }

            lps[i] = len;
        }

        int prefixLen = lps[n - 1];
        string suffix = s.substr(prefixLen);

        reverse(suffix.begin(), suffix.end());
        return suffix + s;
    }
};