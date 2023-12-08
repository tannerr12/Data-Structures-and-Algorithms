class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        
        
        np = []
        
        for i in range(len(prices)):
            np.append((prices[i], profits[i],i))
        
        np.sort(key=lambda x:(x[0], -x[1]))

        left = []
        bestLeft = [0] * len(prices)
        i = 0
        last = -1
        pending = []
        for x,y,z in np:
            if last != x:
                while pending:
                    b,c = pending.pop()
                    idx = bisect_right(left,b,key=lambda x:x[0])
                    idx -= 1
                    if idx < 0 or idx >= len(left) or left[idx][1] < c:
                        insort(left,(b,c))
                    idx = bisect_right(left,b,key=lambda x:x[0])
                    while idx < len(left) and left[idx][1] <= c:
                        left.pop(idx)
                
            #print(left)

                #insort(left,(z, y))
            pending.append((z,y))
            #idx = bisect_right(left,z,key=lambda x:x[0])
            #while idx < len(left) and left[idx][1] <= y:
            #    left.pop(idx)

            
            idx = bisect_left(left,z,key= lambda x:x[0])
            idx -=1
            if idx >= 0:
                bestLeft[i] = left[idx][1]
            
            i+=1
            last = x
            
        left = []
        pending = []
        bestRight = [0] * len(prices)
        i = len(np)-1
        last = -1
        for x,y,z in reversed(np):
            if last != x:
                while pending:
                    b,c = pending.pop()
                    idx = bisect_right(left,b,key=lambda x:x[0])
                    if idx < 0 or idx >= len(left) or left[idx][1] < c:
                        insort(left,(b,c))
                    idx = bisect_left(left,b,key=lambda x:x[0])
                    idx -= 1
                    while idx < len(left) and idx >= 0 and left[idx][1] <= c:
                        left.pop(idx)
                        idx = bisect_left(left,b,key=lambda x:x[0])
                        idx -= 1
                    
            #idx = bisect_right(left,z,key=lambda x:x[0])
            pending.append((z,y))
            #if idx < 0 or idx >= len(left) or left[idx][1] < y:

                
                
            #idx = bisect_left(left,z,key=lambda x:x[0])
            #idx -= 1
            #while idx < len(left) and idx >= 0 and left[idx][1] <= y:
            #    left.pop(idx)
            #    idx = bisect_left(left,z,key=lambda x:x[0])
            #    idx -= 1

            idx = bisect_right(left,z,key= lambda x:x[0])
      
            if idx >= 0 and idx < len(left):
                bestRight[i] = left[idx][1]
            
            i-=1
            last = x
        
        #print(np)
        #print(bestLeft)
        #print(bestRight)
        res = -1
        for i in range(len(np)):
            if bestLeft[i] > 0 and bestRight[i] > 0:
                res = max(res, bestLeft[i] + bestRight[i] + np[i][1])
        
        return res 
            