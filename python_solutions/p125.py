class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join( char.lower() for char in s if char.isalnum())

        start = 0
        end = len(result)-1

        while start < end:
            
            if result[start]!=result[end]:
                return False

            else:
                start+=1
                end-=1
        return True


#space optimized solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True