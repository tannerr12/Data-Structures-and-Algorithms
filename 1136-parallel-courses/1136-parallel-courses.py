class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        
        
        adj = defaultdict(list)
        pre = defaultdict(set)
        s = [i+1 for i in range(n)]
        s = set(s)
        for x,y in relations:
            adj[y].append(x)
            pre[x].add(y)
            if x in s:
                s.remove(x)
            if y in adj[x]:
                return -1
            
        #print(s)
        leaf = []
        
        for key,val in adj.items():
            if len(val) == 0:
                leaf.append(key)
            
        
        if len(leaf) == 0:
            return -1
        
        q = deque()
        
        seen = set()
        for val in s:
            q.append(val)
            seen.add(val)
        
        
        level = 0
        while q:
            
            for i in range(len(q)):
                v = q.popleft()
                
                for a in adj[v]:
                    pre[a].remove(v)
                    
                    if a not in seen and len(pre[a]) == 0:            
                        seen.add(a)
                        q.append(a)
            
                
            level +=1
        return level