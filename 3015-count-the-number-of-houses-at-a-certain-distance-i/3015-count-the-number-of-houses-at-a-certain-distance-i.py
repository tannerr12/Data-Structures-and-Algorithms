class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        adj = defaultdict(list)
        
        for i in range(2,n+1):
            adj[i-1].append(i)
            adj[i].append(i-1)
        
        adj[x].append(y)
        adj[y].append(x)
        
        
        x,y = min(x,y), max(x,y)
        
        ans = [0] * n
        
        
        calc = defaultdict(int)
        
        def bfs(i):
            
            q = deque()
            q.append(i)
            
            seen = set()
            seen.add(i)
            dist = 0
            while q:
                
                for i in range(len(q)):
                    
                    node = q.popleft()
                    calc[dist] += 1
                    
                    for val in adj[node]:
                        
                        if val not in seen:
                            seen.add(val)
                            q.append(val)
                        
                dist += 1
                
        
        for i in range(1,n+1):
            bfs(i)
        
        
        
        for key,val in calc.items():
            if key == 0:
                continue
            ans[key-1] = val
        
        return ans
                