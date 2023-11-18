from sortedcontainers import SortedList
class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        
        #at any given point j what is the max profit value to the left which is less than j
        #what is the max profit to the right where the price is larger
        
        #    <-
        #10, 2 , 3, 4
        #[0, 0 , 2, 7]
        
        #(2,2) , (3,7), (4,10)  

                     
        #(1,38),(3,8), (12, 81), (11,84)  
        #inc = [] 
        n = len(prices)
        sl = SortedList([(float('-inf'),float('-inf'))])
        left = [0]*n
        for i,p in enumerate(prices):
            j = sl.bisect_left((p,profits[i]))
            while j < len(sl) and profits[i] >= sl[j][1]:
                sl.pop(j)
            if profits[i] > sl[j-1][1]:
                sl.add((p,profits[i]))
            j = sl.bisect_left((p,float('-inf')))
            left[i] = sl[j-1][1]

            
        
        n = len(prices)
        sl = SortedList([(float('inf'),float('-inf'))])
        right = [0]*n
        for i in range(n-1,-1,-1):
            p = prices[i]
            j = sl.bisect_right((p,profits[i]))
            while j > 0 and profits[i] >= sl[j-1][1]:
                sl.pop(j-1)
                j = sl.bisect_right((p,profits[i]))
            if profits[i] > sl[j][1]:
                sl.add((p,profits[i]))
            j = sl.bisect_right((p,float('inf')))
            right[i] = sl[j][1]
  

        #12:81, 11:84
                
        res = -1
        for i in range(1, len(prices)-1):
            
            res = max(res, left[i] + profits[i] + right[i])
        
        return res if res != float('-inf') else -1
      