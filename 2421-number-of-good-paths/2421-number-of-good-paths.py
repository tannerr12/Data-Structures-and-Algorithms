class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        parent = [i for i in range(n)]
        rank = [0] * n 
        
        def find(p):
            
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        
        def union(v1,v2):
            
            p1,p2 = find(v1), find(v2)
            
            
            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]:
                
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            else:
               
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
        
        valIndex = defaultdict(list)
        
        
        for i, val in enumerate(vals):
            
            valIndex[val].append(i)
        
        
        res = 0
        
        for val in sorted(valIndex.keys()):
            for i in valIndex[val]:
                for nei in adj[i]:
                    if vals[nei] <= vals[i]:
                        union(i,nei)
        
            count = defaultdict(int)
        
            for i in valIndex[val]:
                count[find(i)] += 1
                res += count[find(i)]
        
        return res
                
            
        
        
        