class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def dfs(i,total):
            
            if total >= len(cost):
                return 0
            if i >= len(cost):
                return float('inf')
            
            res = float('inf')
            
            #take
            res = min(res, dfs(i+1, total + time[i] + 1) + cost[i])
            
            #dont
            res = min(res, dfs(i+1, total))
            
            return res
        
        return dfs(0, 0)
            
            
            
            
            
            
        
        
        