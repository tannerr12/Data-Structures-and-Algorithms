class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        
        n = len(regular)
        
        #dp1 = [0] * n 
        #dp2 = [0] * n
        #base cases
        dp1Prev = regular[0]
        
        dp2Prev = express[0] + expressCost
        
        res = [min(dp1Prev, dp2Prev)]
        
        for i in range(1,n):
            #left option is just straight
            dp1 = min(dp1Prev + regular[i], dp2Prev + regular[i])
            dp2 = min(dp2Prev + express[i], dp1Prev + expressCost + express[i])
            res.append(min(dp1, dp2))
            dp1Prev = dp1
            dp2Prev = dp2
            
        
        
        return res
        """ 
        n = len(regular)
        adj = defaultdict(list)
        for i in range(len(regular)):
            
            adj[('r',i)].append(('r',i+1,regular[i]))
            adj[('r', i)].append(('e',i, expressCost))
            adj[('e', i)].append(('e', i+1, express[i]))
            adj[('e', i)].append(('r', i, 0))
            
        
        
        adj[('e'), n].append(('r', n, 0))
        
        
        #print(adj)
        
        heap = []
        
        heappush(heap, [0, 0, 'r'])
        dp = [float('inf')] * n
        seen = set()
        #print(dp)
        while heap:
            
            weight, num, ty = heappop(heap)
            
            if (num,ty) in seen:
                continue
            
            seen.add((num,ty))
            if ty == 'r' and num > 0:
                dp[num-1] = min(dp[num-1], weight)
            
            for x,y,z in adj[(ty,num)]:
                if (y,x) in seen:
                    continue
                heappush(heap, [weight+z,y,x])
        
        
        
        return dp
        """
        
        
            