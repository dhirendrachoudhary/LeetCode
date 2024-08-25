class Solution:
    def ncr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i+1)
        
        return int(res)
    
    
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for row in range(1, numRows+1):
            innerTriangle = []
            for col in range(1, row+1):
                innerTriangle.append(self.ncr(row-1, col-1))
            
            pascal.append(innerTriangle)
        
        return pascal
    
    