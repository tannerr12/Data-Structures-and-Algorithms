class Solution:
    def minimumTotalPrice(self, N: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        count = [0] * N
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        
       
        def calculate(start,end):
            
            q = deque()
            best = [float('inf')] * N
            parent = [-1] * N
            
            q.append(start)
            
            best[start] = 0
            
            while q:
                
                now = q.popleft()
                
                if now == end:
                    break
                    
                
                for v in adj[now]:
                    #what is the cheapest way to get to this node in terms of distance
                    if best[v] > best[now] + 1:
                        best[v] = best[now] + 1
                        q.append(v)
                        #assign the parent of the new node to now
                        parent[v] = now
            
            current = end
            
            #go backwards and add up all the counts seen
            while parent[current] != -1:
                count[current] +=1
                current = parent[current]
            
            count[start] +=1
        
        for x,y in trips:
            calculate(x,y)
        
        #get the sum of the tree after multiplying the counts but also try all combinations of used and not used and find the minimum combination
        @cache
        def findCost(node,par, used):
            
            res = float('inf')
            if not used:
                
                score = (price[node] // 2) * count[node]
                
                for v in adj[node]:
                    if v != par:
                        score += min(res,findCost(v,node, True))
                
                res = min(res, score)
                
                
            score = price[node] * count[node]

            for v in adj[node]:
                if v != par:
                    score += min(res,findCost(v,node, False))

            res = min(res, score)
            return res
        
 
        return findCost(0,-1,False)
