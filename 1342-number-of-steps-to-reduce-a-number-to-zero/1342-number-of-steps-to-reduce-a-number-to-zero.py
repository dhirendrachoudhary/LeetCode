class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        
        while True:
            if num == 0:
                return steps
            
            if num%2==0:
                num = num//2
                steps += 1
            else:
                num = num - 1
                steps += 1
            
        return steps