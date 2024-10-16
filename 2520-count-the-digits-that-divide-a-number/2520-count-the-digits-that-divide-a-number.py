class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        copyNum = num
        while copyNum > 0:
            oneDigit = copyNum % 10
            copyNum = copyNum // 10
            if num % oneDigit == 0:
                count += 1
        
        return count