class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        res = 0
        cur = 1
        for i in range(1, len(prices)):
            if prices[i-1] != prices[i] +1:
                res += (cur * (cur + 1)) // 2
                cur = 1
            
            else:
                cur += 1
                
        
        res += (cur * (cur + 1)) // 2
        
        return res