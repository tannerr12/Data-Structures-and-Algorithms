class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        
        @cache
        def dfs(i, time):
            
            if i >= len(satisfaction):
                return 0
            
            res = 0
            #add dish
            
            res = max(res,dfs(i+1, time +1) + time * satisfaction[i])
            
            
            #dont add dish
            
            res = max(res, dfs(i+1,time))
            
            return res
        
        
        
        return dfs(0,1)
        