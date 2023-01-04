class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
      
        price.sort()
        
        
        
        def check(val):
            
            count = 1
            lastP = price[0]
            for i in range(1,len(price)):
                
                if price[i] - lastP >= val:
                    count+=1
                    lastP = price[i]
                
                
            return count >= k
        
        
        l,r = 0, price[-1] - price[0]
        while l <= r:
            
            curr = (l+r) // 2
            
            if check(curr):
                l=curr+1
            
            else:
                r = curr -1
                
        
        
        return l -1
                
            
                
            
        