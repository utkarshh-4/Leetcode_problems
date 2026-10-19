class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.length()!=t.length()){
            return false;
        }

        unordered_map<char,int>count;

        for (char ch : s){
            count[ch]++;
        }

        for(char j : t){
            if (count[j]==0){
                return false;
            }

            count[j]--;
            }
            
        return true;
    }
};