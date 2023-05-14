class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        minHeap = []
        mxHeap = []
        
        
        for i in range(len(orders)):
            
            p,a,o = orders[i]
            
            if o == 0:
                
                while minHeap and a and minHeap[0][0] <= p:
                    val,amount = heappop(minHeap)
                    
                    if amount > a:
                        amount -= a
                        a = 0
                        heappush(minHeap, [val, amount])
                    else:
                        a -= amount
                
                if a:
                    heappush(mxHeap, [-p, a])
            
            elif o == 1:
                
                while mxHeap and a and mxHeap[0][0] <= -p:
                    val,amount = heappop(mxHeap)
                    val = -val
                    
                    if amount > a:
                        amount -= a
                        a = 0
                        heappush(mxHeap, [-val, amount])
                    else:
                        a -= amount
                
                if a:
                    heappush(minHeap, [p, a])
        
        
        #print(mxHeap)
        #print(minHeap)
        
        res = 0
        while mxHeap:
            
            v,a = heappop(mxHeap)
            res += a
        
        while minHeap:
            
            v,a = heappop(minHeap)
            res += a
        
        MOD = 10 ** 9 + 7
        return res % MOD