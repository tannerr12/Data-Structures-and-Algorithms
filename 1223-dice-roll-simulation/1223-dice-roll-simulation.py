class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        
        @cache
        def backtrack(i,prev,consec):
            
            if i >= n:
                return 1
            
            res = 0
            for j in range(6):
                
                if j == prev and rollMax[j] - consec > 0:
                    
                    res += backtrack(i+1,j,consec+1)
                
                elif j != prev and rollMax[j] > 0:
                    
                    res += backtrack(i+1,j,1)
                    
            
            
            return res
        
        return backtrack(0,-1,0) % (10**9 + 7)