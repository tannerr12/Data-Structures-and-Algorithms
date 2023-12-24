class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            idx = -1
            for i in range(len(n)):
                if int(n[i]) < x:
                    idx = i
                    break
            
            if idx == -1:
                idx = len(n)
            return n[:idx] + str(x) + n[idx:]
    
        else:
            idx = -1
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    idx = i
                    break
            
            if idx == -1:
                idx = len(n)
            return n[:idx] + str(x) + n[idx:] 
                