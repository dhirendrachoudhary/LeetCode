class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original_x = x
        reverse = 0
        while x > 0:
            remainder = x % 10
            reverse = (reverse * 10) + remainder
            x = x // 10
            
        return reverse == original_x
            