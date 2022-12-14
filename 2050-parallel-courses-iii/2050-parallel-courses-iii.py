class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        
        
        indegree = defaultdict(int)
        adj = defaultdict(list)
        maxTime = time.copy()  
        
        for x,y in relations:
            
            adj[x].append(y)
            indegree[y]+=1

        q = []

        for i in range(1, n +1):
            
            if indegree[i] == 0:
                heapq.heappush(q,(time[i-1], i))
          
        
        
        while q:
                
            t, node = heapq.heappop(q)

            for x in adj[node]:
                    
                indegree[x] -=1
                maxTime[x-1] = max(maxTime[x-1], time[x-1] + maxTime[node-1])
                if indegree[x] == 0:
                    heapq.heappush(q, (maxTime[x-1], x))
                    #seen.add(x)
            

        
        return max(maxTime)
        
                    
                
        
        