class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        
        @cache
        def dfs(i,j):
            
            if i > j:
                return 0
            elif i == j:
                return 1
            
            res = float('inf')
            
            res = min(res, dfs(i + 1, j) + 1)
            
            if arr[i] == arr[i+1]:
                res = min(res, dfs(i+2, j) + 1)
            
            #all other cases
            
            for k in range(i + 2, j+1):
                
                if arr[k] == arr[i]:
                    res = min(res, dfs(k+1,j) + dfs(i+1, k-1))
          
            return res
        
        
        return dfs(0, len(arr) -1)
                
                
                    