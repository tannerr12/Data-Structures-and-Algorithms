class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            indegree[x] += 1
            indegree[y] +=1
            
        q = deque()
        seen = set()
        for key,val in indegree.items():
            if val == 1:
                q.append(key)
                seen.add(key)
        
        size = n
        
        while q and size > 2:
            
            for i in range(len(q)):
                node = q.popleft()
                
                size -=1
                for val in adj[node]:
                    if val in seen:
                        continue
                    indegree[val] -=1
                    if indegree[val] == 1:
                        seen.add(val)
                        q.append(val)
        
        return q
                
            