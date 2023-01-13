class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        adj = defaultdict(list)
        
        for i,x in enumerate(parent):
            
            if x == -1:
                continue
            if s[x] == s[i]:
                continue
            adj[x].append(i)
            adj[i].append(x)
        seen = set()
        res = 0
      
        def dfs(node,parent):
            nonlocal res
            seen.add(node)
            
  
            heap = []
            for child in adj[node]:
                if child == parent:
                    continue
                heappush(heap, -dfs(child,node))
            l =0
            r =0
            if len(heap) >= 2:
                l = heappop(heap)
                r = heappop(heap)
                l = -l
                r = -r
                res = max(res, l+r+1)
            elif len(heap)==1:
                l = heappop(heap)
                l= -l
                res = max(res, l+1)
                
            res = max(res, l+r + 1)
            return max(l,r) + 1
        
        for i in range(len(parent)):
            if i not in seen:
                dfs(i,-1)
        return res
            
                
                
            
            