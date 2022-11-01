class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        h1 = []
        h2 = []
        
        
        for i in range(len(timePoints)):
            t = timePoints[i]
            
            #convert to number
            f,b = t[:2],t[3:]
            
            
            h = int(f) * 60 + int(b) 
            num = h
            heapq.heappush(h1,num)
            if num <= 720:
                num+=720
            else:
                num -= 720
            heapq.heappush(h2,num)
            #heapq.heappush(h2,-num)
            
        
        
        
       # print(h)
        
        
        res = float('inf')
        
        prev = heapq.heappop(h1)
        while h1:
            
            t1 = heapq.heappop(h1)
            
            res = min(res,abs(t1 - prev))
            
            prev = t1
        
        prev = heapq.heappop(h2)
        while h2:
            
            t1 = heapq.heappop(h2)
            
            res = min(res,abs(t1 - prev))
            
            prev = t1
        #t2  = heapq.heappop(h2)
        #t2 = -t2
    

       # res = min(res, abs(t1 - h1[0]), abs(t2 - -h2[0]), abs(t2 - t1))
            
        print(res)
        
        
        return res
        