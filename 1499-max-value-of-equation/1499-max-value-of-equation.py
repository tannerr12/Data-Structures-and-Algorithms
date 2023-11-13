#from sortedcontainers import SortedList
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        #[[1,3],[2,0],[5,10],[6,-10]], k = 1
        
        #exploring SortedList, BIT, binary search
        #1,2,5,6
        
        
        #1,2,5,6
        
        
        #3
        
        
        #[1,2,5,6]
        
        #[0,2]
        
        
        #4
        
        #2, -2, 5, -16

            
        #print(nPoints)
        l = 0
        sl = []
        res = float('-inf')
        for i in range(len(points)):
            while sl and points[i][0] - points[sl[0][1]][0] > k:
                heappop(sl)
            
            if len(sl) > 0:
                b = sl[0][1]
                res = max(res, points[i][0] - points[b][0] + points[i][1] + points[b][1]) 
            heappush(sl,(-(points[i][1] - points[i][0]), i))
        
        return res