class Solution:
    def canWin(self, currentState: str) -> bool:
        


        @cache
        def dfs(curr):
            
            for i in range(len(curr) -1):
                if curr[i] == curr[i +1] == '+':
                    ans = dfs(curr[:i] + '--' + curr[i+2:])
                    if not ans:
                        return True
            return False
        
        
        return dfs(currentState)
        
            