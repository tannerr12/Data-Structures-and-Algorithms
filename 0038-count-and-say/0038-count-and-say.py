class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        
        
        def dfs(n):
            
            if n == 1:
                return '1'
            
            
            
            prev = dfs(n-1)
            res = ''
            c = 1
            
            
            
            for i in range(len(prev)):
                
                if i == len(prev) -1 or prev[i] != prev[i+1]:
                    res += str(c) + prev[i]
                    c=1
                else:
                    c+=1
                    
                
            
            return res
        
        
        return dfs(n)