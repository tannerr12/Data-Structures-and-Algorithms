class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
        #2x dfs and store path the target in another set
        #first we find from 1 node to target saving its path than dfs a from the second
        #node and if we find a node we have seen before in that path we return it
        seen =set()
        optimalPath = set()
        def dfs(node,parent,target):
            nonlocal optimalPath
            seen.add(node)
            if node == target:
                optimalPath = seen.copy()
                seen.remove(node)
                return  
            
            for val in adj[node]:
                
                if val == parent or val in seen:
                    continue
                
                dfs(val,node,target)
                
            seen.remove(node)   
        
        def dfs2(node,parent):
            nonlocal optimalPath
            
            if node in optimalPath:
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
   
        return res
            
            
        