class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        #create a map of compliments
        mp = defaultdict(int)
        
        
        for r in matrix:
            
            s = ''
            compliment = False
            
            if r[0] == 1:
                compliment = True
            
            for val in r:
                
                if compliment:
                    s += str(val ^ 1)
                else:
                    s += str(val)
                    
            
            mp[s] +=1
        
        
        return max(mp.values())
                