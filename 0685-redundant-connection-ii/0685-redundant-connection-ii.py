class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        nodes = len(edges)
        
        graph = defaultdict(set)
        parent = set([i for i in range(1, len(edges) + 1)])
        count = defaultdict(int)
        for x,y in edges:
            graph[x].add(y)
            count[y] += 1
            if y in parent:
                parent.remove(y)
        
        par = list(parent)
        
        
        def scan(par):
            nonlocal nodes
            q = deque([par])
            seen = set()
            seen.add(par)
            while q:
                
                node = q.popleft()
                
                for val in graph[node]:
                    
                    if val in seen:
                        return False
                    
                    seen.add(val)
                    q.append(val)
            
            return len(seen) == nodes
                
            
        
        for i in range(len(edges)-1,-1,-1):
            x,y = edges[i]
            #remove the edge
            graph[x].remove(y)
            count[y] -= 1
            if (count[y] != 0 and len(par) > 0) or (len(par) == 0 and count[y] == 0):
                #scan and make sure we dont hit a cycle and hit all nodes
                if len(par) > 0:
                    if scan(par[0]):
                        return edges[i]
                else:
                    if scan(y):
                        return edges[i]
                    
            #add it back
            graph[x].add(y)
            count[y] += 1
        
        
        
        
        