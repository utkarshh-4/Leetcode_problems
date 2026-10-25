class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, end = 0;
        int n = s.length();

        for (int center = 0; center < n; center++) {
            // Odd-length palindrome
            int left = center, right = center;

            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left > end - start) {
                    start = left;
                    end = right;
                }

                left--;
                right++;
            }

            // Even-length palindrome
            left = center;
            right = center + 1;

            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left > end - start) {
                    start = left;
                    end = right;
                }

                left--;
                right++;
            }
        }

        return s.substr(start, end - start + 1);
    }
};