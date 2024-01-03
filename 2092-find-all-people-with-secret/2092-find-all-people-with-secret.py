class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
    
        adj = defaultdict(lambda:defaultdict(list))
        
        
        
        for x,y,z in meetings:
            adj[z][x].append(y)
            adj[z][y].append(x)
    
        
        people = set()
        people.add(0)
        people.add(firstPerson)
        
        for t in sorted(adj):
            q = deque()
            for val in adj[t]:
                if val in people:
                    q.append(val)
            
            while q:
                
                for i in range(len(q)):
                    
                    node = q.popleft()
                    
                    for val in adj[t][node]:
                        
                        if val in people:
                            continue
                        
                        people.add(val)
                        q.append(val)
        
        return people
                    