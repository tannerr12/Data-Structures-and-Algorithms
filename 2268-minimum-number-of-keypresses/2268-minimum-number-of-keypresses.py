class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        heap = []
        res = 0
        h = Counter(s)
        
        
        for key,val in h.items():
            
            heapq.heappush(heap, (-val,key))
            
        
        
        
        #print(heap)
        
        num = 0
        while heap:
            
            num+=1
            val,key = heapq.heappop(heap)
            val = -val
            multi = math.ceil(num/9) 
            
            res += val * multi
            
        
        
        return res
                
              
            