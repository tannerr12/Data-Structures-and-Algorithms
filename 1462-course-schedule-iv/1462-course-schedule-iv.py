class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        mp = defaultdict(set)
        
        
        for x,y in pre:
            
            adj[x].append(y)
            
        
        for i in range(n):
            
            q = deque()
            q.append(i)
            seen = set()
            seen.add(i)
            
            while q:
                
                for j in range(len(q)):
                    
                    node = q.popleft()
                    
                    if node != i:
                        mp[i].add(node)
                        
                    
                    for val in adj[node]:
                        if val not in seen:
                            seen.add(val)
                            q.append(val)
            
        
        #print(mp)
        res = []
        for x,y in queries:
            if y in mp[x]:
                res.append(True)
            else:
                res.append(False)
            
        return res