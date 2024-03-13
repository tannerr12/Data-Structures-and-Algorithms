class Solution:
    def pivotInteger(self, n: int) -> int:
        
        
        sumL = 0
        sumR = 0
        memoL = {}
      
        for i in range(1,n+1):
            memoL[i] = (i * (i+1)) //2
            
        for i in range(n,0,-1):
            
            sumR += i
            
            if memoL[i] == sumR:
                return i
        
        return -1
            