import re
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        
        if len(s) == 1 or len(s) == 0:
            return True
        
        left = 0
        right = len(s) - 1
        reverse = False
        while left < right:
            if s[left] == s[right]:
                reverse = True
            else:
                return False
            left += 1
            right -= 1
        return reverse