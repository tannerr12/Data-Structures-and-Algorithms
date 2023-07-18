class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        adj = defaultdict(list)
        
        for i in range(len(parents)):
            if parents[i] != -1:
                adj[parents[i]].append(i)
                
        
        mp = defaultdict(int)
        def dfs(node):
            
            if node is None:
                return 0
            
            p,s = 1,0
            res = 0
            
            for child in adj[node]:
                
                res = dfs(child)
                
                p *= res
                s += res
                
            
            p *= max(1,len(parents) - 1 - s)
            
            mp[p] += 1
            
            return s + 1
        
        dfs(0)
        
        return mp[max(mp.keys())]
    
    

           