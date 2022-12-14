class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key= lambda x: x[0])

        
        res = 1
        i=1
        prevEnd = points[0][1]
        prevStart = points[0][0]
        while i < len(points):
            
            if (points[i][0] > prevEnd) and (points[i][1] > prevEnd):
                res +=1
                prevEnd = points[i][1]
                prevStart = points[i][0]
            
            else:
                prevEnd = min(prevEnd, points[i][1])
                prevStart = max(prevStart, points[i][0])
            
            i+=1
        
        return res
            
            
            
            