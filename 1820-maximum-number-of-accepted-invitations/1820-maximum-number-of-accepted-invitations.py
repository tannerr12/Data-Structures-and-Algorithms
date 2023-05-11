class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        adj = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    adj[i].append(j)
    
        
        match = {}
        
        def dfs(i,seen):
            
            for val in adj[i]:
                if val in seen:
                    continue
                seen.add(val)
                if val not in match or dfs(match[val], seen):
                    
                    match[val] = i
                    return True
                    
        
        for i in range(m):            
            dfs(i,set())
        
        
        return len(match)
        
        
                    
            
                
                