class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        start=0
        end=0

        for center in range(n):
            left=center
            right=center

            while left>=0 and right<n and s[left]==s[right]:

                if right - left > end-start:
                    start=left
                    end=right

                left-=1
                right+=1

            left=center
            right=center+1

            while left>=0 and right<n and s[left]==s[right]:
                if right-left>end-start:
                    start=left
                    end=right

                left-=1
                right+=1
        
        return s[start:end+1]