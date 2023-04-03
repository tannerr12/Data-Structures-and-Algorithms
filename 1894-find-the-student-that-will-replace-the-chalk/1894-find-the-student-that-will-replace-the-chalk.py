class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        c = sum(chalk)
        
        am = k // c
        
        k-= c * am
        
        #print(k)
        
        
        for i in range(len(chalk)):
            
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
                
            
            
            