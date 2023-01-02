class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dfs(start,end):
            
            if start >= end:
                return 1
            
            
            res = 0
            
            for i in range(start, end):
                
                left = dfs(start,i)
                right = dfs(i+1,end)
                
                res += left * right
                    
                
            
            return res
        
        return dfs(0,n)
