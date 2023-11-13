from sortedcontainers import SortedList
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
        
        nPoints = []
        
        for i, (x,y) in enumerate(points):
            nPoints.append((y-x, i))
            
        #print(nPoints)
        l = 0
        sl = SortedList()
        res = float('-inf')
        for i, val in enumerate(nPoints):
            while sl and points[l][0] < points[i][0] - k:
                idx = bisect_left(sl,(points[l][1] - points[l][0],l),key = lambda x: (x[0], x[1]))
                sl.pop(idx)
                l+=1
            
            if len(sl) > 0:
                b = sl[-1][1]
                res = max(res, points[i][0] - points[b][0] + points[i][1] + points[b][1]) 
            sl.add(val)
        
        return res