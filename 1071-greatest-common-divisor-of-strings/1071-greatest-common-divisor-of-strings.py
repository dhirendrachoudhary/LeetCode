class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: manual Euclidean algorithm for gcd of lengths
        def manual_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        gcd_len = manual_gcd(len(str1), len(str2))
        
        # Step 3: return gcd prefix
        return str1[:gcd_len]