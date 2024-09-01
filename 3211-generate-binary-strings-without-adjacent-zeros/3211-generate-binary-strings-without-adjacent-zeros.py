class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        
        arr = []
        
        def dfs(word):
            
            if len(word) == n:
                arr.append(word)
                return
            
            
            if len(word) > 0 and word[-1] == '0':    
                dfs(word + '1')
            
            else:
                dfs(word + '1')
                dfs(word + '0')
                
            
            
        
        dfs('')
        
        return arr
        
            
            
            