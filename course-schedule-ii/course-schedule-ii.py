class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(set)
        related = defaultdict(list)
        for x,y in prerequisites:
            adj[x].add(y)
            related[y].append(x)
        
        
        q = deque()
        
        for i in range(numCourses):
            if len(adj[i]) == 0:
                q.append(i)
              
        seen = set()
        res = []
        while len(res) != numCourses and q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                res.append(node)
                seen.add(node)
                for val in related[node]:
                    if val in seen:
                        continue
                    adj[val].remove(node)
                    if len(adj[val]) == 0:
                        q.append(val)
        
        return res if len(res) == numCourses else []
                
        
        
        
            