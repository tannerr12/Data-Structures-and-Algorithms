class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        adj = defaultdict(list)
        indegree = defaultdict(int)
        

        for x,y in relations:

            adj[x].append(y)
            indegree[y] +=1
        
        #perform bfs
        q = deque()

        for i in range(1, n+1):
            if i not in indegree:
                q.append(i)
        
        level = 0
        seen2 = set()
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
              
                seen2.add(node)
                for x in adj[node]:
                    
                    indegree[x] -=1
                    if indegree[x] == 0:
                        q.append(x)
                
            
            level +=1
                


        if len(seen2) == n:
            return level 
        return -1


