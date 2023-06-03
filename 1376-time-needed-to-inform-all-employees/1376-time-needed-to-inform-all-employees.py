class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        
        for i in range(len(manager)):
            
            if manager[i] == -1:
                continue
            
            adj[manager[i]].append([i,informTime[manager[i]]])   

            
        #print(adj)
        q = deque()
        q.append([headID,0])
        seen = set()
        seen.add(headID)
        res = 0
        while q:
            
            for i in range(len(q)):
                
                idx, cost = q.popleft()
                res = max(res, cost)
                seen.add(idx)
                
                for x,c in adj[idx]:
                    
                    if x in seen:
                        continue
                    
                    q.append([x, c + cost])
        return res