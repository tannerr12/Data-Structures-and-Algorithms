class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(n):
            indegree[i] = 0
        for x,y in relations:
            adj[x].append(y)
            indegree[y]+=1
        
        
        q = deque()
        seen = set()
        for key,val in indegree.items():
            if val == 0:
                q.append(key)
                seen.add(key)             
        years = 0
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                for val in adj[node]:
                    if val in seen:
                        continue
                    
                    indegree[val] -=1
                    if indegree[val] == 0:
                        q.append(val)
                        seen.add(val)

            years +=1
        
        return years if sum(indegree.values()) == 0 else -1
        