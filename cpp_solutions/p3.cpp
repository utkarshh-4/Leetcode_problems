//optimized using the array

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> lastSeen(128, -1);
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            unsigned char c = s[right];

            left = max(left, lastSeen[c] + 1);
            lastSeen[c] = right;

            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};

//optimized using unordered_set

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_length=0;
        int left = 0;
        unordered_set<char>seen;

        for( int right=0; right<s.length() ; right++){
            while( seen.count(s[right])){
                seen.erase(s[left]);
                left++;
            }

            seen.insert(s[right]);

            max_length = max(max_length,right-left+1);
        }
        
        return max_length;
    }
};