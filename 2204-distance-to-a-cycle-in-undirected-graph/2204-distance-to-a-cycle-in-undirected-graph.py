class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        ans = [float('inf')] * n
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        #step 1 find the location of the cycle and which nodes are included
        
        seen = set()
        path = []
        p = []
        
        def dfs(node,par):
            nonlocal p
            if p:
                return
            if node in seen:
                p = path.copy()
                return
            seen.add(node)
            for v in adj[node]:
                if v == par:
                    continue
                path.append(v)
                dfs(v,node)
                path.pop()
                
        
        path.append(0)
        dfs(0, -1)
        
        end = p[-1]
        cycle = set()
        cycle.add(p.pop())
        while p and p[-1] != end:
            cycle.add(p.pop())
        
        #print(cycle)
        seen = set()
        q = deque()
        for val in cycle:
            q.append(val)
        level = 0
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                if node in seen:
                    continue
                ans[node] = level
                seen.add(node)
                
                for v in adj[node]:
                    
                    if v in seen:
                        continue
                    
                    q.append(v)
                    
            level +=1
        
        return ans