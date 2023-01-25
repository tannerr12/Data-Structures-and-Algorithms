class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        adj = defaultdict(list)
        for i,x in enumerate(edges):
            
            adj[i].append(x)

        q = deque()
        
        q.append([0,node1,1])
        
        q.append([0, node2,0])
        
        seen1 = set()
        seen2 = set()
        res = []
        while q:
            
            
            for i in range(len(q)):
                
                count, node, flag = q.popleft()
                
                if len(res) > 0 and count > res[0][0]:
                    continue
                
                if flag:
                    if node in seen1:
                        continue
                    seen1.add(node)
                else:
                    if node in seen2:
                        continue
                    seen2.add(node)
                    
                
                if node in seen1 and node in seen2:
                    res.append([count, node])
                
                for n in adj[node]:
                    
                    q.append([count + 1, n, flag])
            
        
        
        
        
        if len(res) == 0:
            return -1
        
        res.sort()
        
        return res[0][1]
        