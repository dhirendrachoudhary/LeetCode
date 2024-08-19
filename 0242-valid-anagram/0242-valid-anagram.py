class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # edge case
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}
        for i in s:
            if i in dictS:
                dictS[i] += 1
            else:
                dictS[i] = 1
        
        for i in t:
            if i in dictT:
                dictT[i] += 1
            else:
                dictT[i] = 1
        anaram = False
        for i in dictS.keys():
            if i in dictT.keys():
                if dictS[i] == dictT[i]:
                    anaram = True
                else:
                    anaram = False
            else:
                return False
        
        return anaram
        