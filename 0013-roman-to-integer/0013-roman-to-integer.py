class Solution:
    def romanToInt(self, s: str) -> int:
        rm_to_int = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
        
        sum = 0
        temp = 0
        for num in s[::-1]:
            
            if temp == 0:
                sum += rm_to_int[num]
            else:                
                if rm_to_int[num] < rm_to_int[temp]:
                    sum -= rm_to_int[num]
                else:
                    sum += rm_to_int[num]
            temp = num
            
        return sum