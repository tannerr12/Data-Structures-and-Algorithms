class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        #a cycle node must have atleast 1 indegree and 1 outdegree
        #just keep track of node counts than if we see the same node again take count - count when we saw that node
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
            
        
        seen = {}
        s2 = set()
       # print(adj)
        @cache
        def dfs(i,par,d):
            
            if i in seen:
                return d - seen[i] 
            seen[i] = d
            s2.add(i)
            res = float('inf')
            for val in adj[i]:
                if val == par:
                    continue
              #  print(val)
              #  print(i)
                v = dfs(val, i, d+1)
                if v > 1:
                    res = min(res,v)
            del seen[i]
            return res
        
        
        
        res = float('inf')
        #res = dfs(6,-1,0)
        for i in range(n):
            #seen = {}
            if i not in s2:
                v = min(res,dfs(i, -1, 0))
                if v == float('inf'):
                    continue
                else:
                    res = v
        return res if res != 0 and res != float('inf') else -1
            
                
            
            
            