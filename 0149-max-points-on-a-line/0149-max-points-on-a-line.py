class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        

        res = 0
        for i in range(len(points)):
            y,x = points[i]
            upDiag = 0
            downDiag = 0
            up = 0
            right = 0
            upD = collections.defaultdict(int)
            dwD = collections.defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                    
                yy,xx = points[j]
                if xx == x:
                    right +=1
                if yy == y: 
                    up+=1
                if xx > x and yy > y:
                    upD[(yy-y) / (xx-x)] += 1     
                if xx < x and yy > y:
                    dwD[(yy-y) / (xx-x)] +=1
            
            
            
            if len(upD) > 0:
                upDiag = max(upD.values())
            if len(dwD) > 0:
                downDiag = max(dwD.values())
            res = max(res, max(right, up,upDiag,downDiag) +1) 
        
        
        
        return res
            
            
            
            
        