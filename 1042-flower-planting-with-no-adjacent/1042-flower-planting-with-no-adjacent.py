class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        
        for x,y in paths:
            adj[x].append(y)
            adj[y].append(x)
            
        res = [0] * n   
        
        for i in range(1,n + 1):
            if res[i-1] != 0:
                continue
            seen = set()

            q = deque([i])

            while q:

                for i in range(len(q)):

                    node = q.popleft()

                    seen.add(node)
                    vals = set()
                    for x in adj[node]:
                        vals.add(res[x-1])
                        if x not in seen:
                            q.append(x)

                    for i in range(1,5):
                        if i not in vals:
                            res[node-1] = i
                            break
        return res
                
            