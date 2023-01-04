class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        
        @cache
        def dfs(i):
            
            if i >= len(tasks):
                return 0
            
            
            res = float('inf')
            #take 3 
            if i + 2 < len(tasks) and tasks[i] == tasks[i+1] == tasks[i+2]:
                res = min(res,dfs(i+3) + 1)
            
            #take 2
            if i + 1 < len(tasks) and tasks[i] == tasks[i+1]:
                res = min(res,dfs(i+2) +1) 
            
        
            
            
            return res
        
        val = dfs(0)
        
        if val == float('inf'):
            return -1
        else:
            return val
            
                
            
            