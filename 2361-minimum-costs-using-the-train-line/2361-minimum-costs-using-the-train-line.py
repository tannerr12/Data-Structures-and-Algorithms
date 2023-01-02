class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        
        n = len(regular)
        
        dp1 = [0] * n 
        dp2 = [0] * n
        #base cases
        dp1[0] = regular[0]
        
        dp2[0] = express[0] + expressCost
        
        res = [min(dp1[0], dp2[0])]
        
        for i in range(1,n):
            dp1[i] = min(dp1[i -1] + regular[i], dp2[i-1] + regular[i])
            dp2[i] = min(dp2[i-1] + express[i], dp1[i-1] + expressCost + express[i])
            res.append(min(dp1[i], dp2[i]))
            
        
        
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
        
        
            