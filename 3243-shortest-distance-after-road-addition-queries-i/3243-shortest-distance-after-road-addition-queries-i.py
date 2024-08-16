class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for i in range(n-1):
            adj[i].append(i+1)
        
        
        
        
        def search():
            
            q = deque([0])
            cost = 0
            seen = set()
            seen.add(0)
            while q:
                
                for i in range(len(q)):
                    node = q.popleft()
                    
                    for val in adj[node]:
                        if val == n-1:
                            return cost + 1
                        if val not in seen:
                            seen.add(val)
                            q.append(val)
                
                
                cost += 1
            
        
        ans = [0] * len(queries)
        for i in range(len(queries)):
            
            x,y = queries[i]
            adj[x].append(y)
            ans[i] = search()
        
        
        return ans
            
                    