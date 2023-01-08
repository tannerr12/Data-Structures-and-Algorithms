class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        
        heapNew = []
        heapOld = []
        heapBL = []
        heapBR = []
        i = 0
        for a,b,c,d in time:
            heappush(heapBL, (-(a + c),-i))
            i +=1
        
        
        t = 0

        while n:
            
            while heapNew and heapNew[0][0] <= t:
                a,i = heappop(heapNew)
                heappush(heapBL, (-time[i][0] - time[i][2], -i))
            while heapOld and heapOld[0][0] <= t:
                a,i = heappop(heapOld)
                heappush(heapBR, (-time[i][0] - time[i][2], -i))
            
            if heapBR:
                x,i = heappop(heapBR)
                t += time[-i][2]
                heappush(heapNew, (t + time[-i][3], -i))
                n-=1
            elif heapBL and n > len(heapBR) + len(heapOld):
                x,i = heappop(heapBL)
                t += time[-i][0]
                heappush(heapOld, (t + time[-i][1], -i))
            else:
                x = heapNew[0][0] if heapNew and n > len(heapBR) + len(heapOld) else float('inf')
                y = heapOld[0][0] if heapOld else float('inf')
                t = min(x,y)
        
        return t

        
        