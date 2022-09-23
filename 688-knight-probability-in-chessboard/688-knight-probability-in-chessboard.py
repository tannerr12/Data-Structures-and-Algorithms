class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        trueCount = 0
        falseCount = 0
        
        numMoves = 0
        memo = {}
        def dfs(r,c, move):
            nonlocal trueCount
            nonlocal falseCount
            nonlocal numMoves
            numMoves +=1
            
            if (r,c,move) in memo:
                return memo[(r,c,move)]
            if r >= n or r < 0 or c >= n or c < 0:
                
                return 0
            
            
            if move == k:
                
                return 1
            
            #move in 8 directions
            ans = 0
            
            ans +=0.125 * dfs(r-2,c-1,move+1)
            ans +=0.125 * dfs(r-2,c+1,move+1)
            ans+= 0.125 * dfs(r-1,c+2,move+1)
            ans +=0.125 * dfs(r-1,c-2,move+1)
            
            ans+=0.125 * dfs(r+1,c-2,move+1)
            ans+=0.125 * dfs(r+2, c-1,move+1)
            ans+=0.125 * dfs(r+1,c+2,move+1)
            ans+=0.125 * dfs(r+2,c+1,move+1)
            
            memo[(r,c,move)] = ans
            return ans
        return dfs(row,column,0)
        
        
        
        
 
        