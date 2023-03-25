class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        colPoints = [points for points in points[0]]
        
        for i in range(1,len(points)):
            mx = float('-inf')
            for j in range(len(points[0])):
                
                mx = max(mx - 1, colPoints[j])
                
                colPoints[j] = mx
                
            mx = float('-inf')
            for j in range(len(points[0]) -1,-1,-1):
                
                mx = max(mx - 1, colPoints[j])
                
                colPoints[j] = mx
                
            
            for j in range(len(colPoints)):
                colPoints[j] = points[i][j] + colPoints[j]
        
        return max(colPoints)