
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        
        stockPrices.sort()
   
        res = 0
   
        psY = None
        psX = None
        for i in range(1,len(stockPrices)):
            cDay,cPrice = stockPrices[i][0], stockPrices[i][1]
            pDay, pPrice = stockPrices[i-1][0], stockPrices[i-1][1]
            
            
            slopex = cDay - pDay
            slopey = pPrice - cPrice
            
            if psY is None or psY * slopex != slopey * psX:
                    res +=1
                
            psY = slopey
            psX = slopex
        

        return res 