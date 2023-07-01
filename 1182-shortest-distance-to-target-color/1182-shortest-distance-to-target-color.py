class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        
        color = [[-1,-1,-1]] * len(colors)
        
        one,two,three = -1,-1,-1
        for i in range(len(colors)):
            
            if colors[i] == 1:
                one = i
            elif colors[i] == 2:
                two = i
            else:
                three = i
            
            color[i] = [one,two,three]
            
        
        colorRight = [[-1,-1,1]] * len(colors)            
        
        
        for i in range(len(colors)-1,-1,-1):
            
            if colors[i] == 1:
                one = i
            elif colors[i] == 2:
                two = i
            else:
                three = i
            
            colorRight[i] = [one,two,three]
        
        
        ans = []
        
        for x,y in queries:
            best = float('inf')
            if color[x][y-1] != -1:
                best = abs(x - color[x][y-1])
            if colorRight[x][y-1] != -1:
                best = min(best,abs(x - colorRight[x][y-1]))
            
            if best == float('inf'):
                best = -1
            ans.append(best)
        
        return ans