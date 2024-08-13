class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.strip().split()
        return len(sp[-1])