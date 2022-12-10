class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        
        adj = defaultdict(list)
        
        
        
        for x,y in edges:
            
            adj[x].append((y, vals[y]))
            adj[y].append((x, vals[x]))
            
            
        res = float('-inf')
        
        for i in range(len(vals)):
            
            
            ls = adj[i]
            
            ls = sorted(ls, key=lambda x : -x[1])
    
            localS = 0
            for j in range(min(k,len(ls))):
                localS += ls[j][1]
                res = max(res,localS+vals[i])
            res = max(res,vals[i])
        
        return res
        
        
        