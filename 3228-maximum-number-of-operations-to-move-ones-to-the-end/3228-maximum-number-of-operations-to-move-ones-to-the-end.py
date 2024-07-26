class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        
        #if its next to a 0 than + 2 else + 1 if wrong pos else 0
    
        #1110000 = 3
        #1010100
        #0110100
        #0101100
        #0011100 = 6
        
        cur = len(s) -1
        last = cur
        lastEdge = True
        countup = 2
        for i in range(len(s)-1,-1,-1):
            
            if s[i] == '1':
                if cur == i:
                    lastEdge = True
                elif last == i + 1 or lastEdge:
                    res += countup - 1
                    lastEdge = False
                else:
                    res += countup
                    countup += 1
                    lastEdge = False
                
                
                last = i
                cur -= 1
        
        return res
                    
                    
                    