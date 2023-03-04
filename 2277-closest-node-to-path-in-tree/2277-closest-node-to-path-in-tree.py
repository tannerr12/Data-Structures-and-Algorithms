class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
        
        seen =set()
        stack = set()
        def dfs(node,parent,target):
            nonlocal stack
            seen.add(node)
            if node == target:
                stack = seen.copy()
                return  
            
            for val in adj[node]:
                
                if val == parent or val in seen:
                    continue
                
                dfs(val,node,target)
                
            seen.remove(node)   
        
        def dfs2(node,parent):
            nonlocal stack
            
            if node in stack:
                return node
            res = None
            for val in adj[node]:
                
                if val == parent:
                    continue
                
                v = dfs2(val,node)
                if v is not None:
                    res = v
            
            return res
                
        
        res = []
        for x,y,z in query:
        
            dfs(x,-1,z)
            
            res.append(dfs2(y,-1))
            seen = set()
        return res
            
            
        