class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        adj = collections.defaultdict(list)
        
        
        for r in range(len(isConnected)):
            
            for c in range(len(isConnected[0])):
                
                if r == c:
                    continue
                if isConnected[r][c] == 1:
                     adj[r].append(c)
                
        
        
        
        visited = {}
        
        def dfs(num):
            
            if num in visited:
                return 0
            
            
            
            visited[num] = 1
            
            for a in adj[num]:
                
                dfs(a)
            
            
            
            
            return 1
        
        
        res = 0
        for key,val in adj.items():
            
            res += dfs(key)
        
        
        return res + len(isConnected) - len(visited)