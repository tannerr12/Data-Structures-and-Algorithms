class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        @cache
        def dfs(i,j):
            
            if i >= len(a):
                return 0
            elif j >= len(b):
                return float('-inf')
            
            best = float('-inf')
            
            #take 
            best = max(best, dfs(i+1, j+1) + a[i] * b[j])
            
            #skip
            best = max(best, dfs(i, j+1))
            
            
            return best
        
        
        
        
        return dfs(0,0)