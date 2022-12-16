class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        
        
        
        adj = defaultdict(list)
        
        for x,y,z in roads:
            
            adj[x].append((y,z))
            adj[y].append((x,z))
            
        
        
        dp = appleCost.copy()
        for node in range(n):
            
            
            
            heap = []
            
            heappush(heap, (0,node+1,False,0 | (1 << node)))
            
            
            while heap:
                
                weight, vert, apple,bitmap = heappop(heap)
                
                if weight >= dp[node]:
                    continue
                
                
                if apple:
                    dp[node] = min(dp[node], weight)
                    continue
                    
                
                for a,w in adj[vert]:
                    """
                    #already apple
                    if apple and bitmap & (1 << (a-1)) == 0:
                        heappush(heap, (weight + w * 2, a, apple,bitmap | (1<< (a-1))))
                    """
                    #need apple
                    if bitmap & (1 << (a-1)) == 0:
                        heappush(heap, (weight + appleCost[a-1] + (w * (k+1)), a, True,0))
                    
                        #skip apple
                        heappush(heap,(weight + (w * (k+1)), a, False, bitmap | (1 << (a-1))))
                    
        
        return dp
                
                
                
                
                
            
        
        
        
        
        