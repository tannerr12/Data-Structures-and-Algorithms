class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
        adj = defaultdict(list)
        for x,y in workers:
            for a,b in bikes:
                manhat = abs((x - a)) + abs((y - b))
                adj[(x,y)].append([manhat, (a,b)])
                
            
            
        
        for w in workers:
            heap = []
            seen = set()
            heapq.heappush(heap,w)
            
            
            
            while heap:
                
                weight, bike = heapq.heappop()
                
                
        """        
        
    
    
    
    
        #dp = [0] * len(workers)
        memo = {}
        
        def backtrack(i,bitmask):
            
            if i >= len(workers):
                return 0
            if (i,bitmask) in memo:
                return memo[(i,bitmask)]
            
            res = float('inf')
            for j in range(len(bikes)):
                if (bitmask & (1 << j)) == 0:
                    manhat = abs((workers[i][0] - bikes[j][0])) + abs((workers[i][1] - bikes[j][1]))
                    res = min(res,backtrack(i+1,bitmask | (1 << j)) + manhat)

                    
                
            memo[(i,bitmask)] = res
            return res
        
        
        return backtrack(0,0)
                
                
                
            
            