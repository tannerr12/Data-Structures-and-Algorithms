class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #group each point by x and y pairs 
        
        #for each x pair find a match 
        s = set()
        ymp = defaultdict(list)
        xmp = defaultdict(list)
        
        for x,y in points:    
            xmp[x].append(y)
            ymp[y].append(x)
            s.add((x,y))
        
        
        ans = float('inf')
        for x,y in points:
            
            for xval in ymp[y]:
                if xval <= x:
                    continue
                for yval in xmp[xval]:
                    if yval <= y:
                        continue
                    if (x, yval) in s:
                        ans = min(ans, abs((xval - x) * (yval - y)))
        
        
        return ans if ans != float('inf') else 0
                        
                    
                    
                    
                