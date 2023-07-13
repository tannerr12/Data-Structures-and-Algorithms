class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        
        res = []
        def backtrack(i,last,st):
            
            if i >= n:
                res.append(st)
                return 
            
            
            for val in 'abc':
                
                if val == last:
                    continue
                
                backtrack(i+1, val, st + val)
            
        
        backtrack(0,'','')
        
        
        res.sort()
        if k > len(res):
            return ''
        return res[k-1]
        
        
            
            
            
            
            