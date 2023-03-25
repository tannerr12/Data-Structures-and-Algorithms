class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        #initialize the first row
        colPoints = [points for points in points[0]]
        
        for i in range(1,len(points)):
            mx = float('-inf')
            
            #while we go through from front to back we keep track of the maxium, each shift costs 1 so we either take the new value
            #or the current max -1 and assign our upper row to this
            for j in range(len(points[0])):
                mx = max(mx - 1, colPoints[j])
                colPoints[j] = mx
            
            
            #same thing but back to front
            mx = float('-inf')
            for j in range(len(points[0]) -1,-1,-1):
                mx = max(mx - 1, colPoints[j])
                colPoints[j] = mx
                
            #we make the upper row the current row so that when we hit the next iteration it will be the upper row again
            for j in range(len(colPoints)):
                #current row + upper rows max
                colPoints[j] = points[i][j] + colPoints[j]
        
        #return max from last row
        return max(colPoints)