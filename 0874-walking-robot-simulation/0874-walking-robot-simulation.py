class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        def calcE(x,y):    
            return (abs(x - 0)**2 + (y - 0)**2)
        
        xaxis = defaultdict(list)
        yaxis = defaultdict(list)
        for x,y in obstacles:
            xaxis[x].append(y)
            yaxis[y].append(x)
        
        for val in xaxis:
            xaxis[val].sort()
        for val in yaxis:
            yaxis[val].sort()
            
        
        #pos = ['+Y', '+X', '-Y', '-X']
        cur = 0
        
        px,py = 0,0
        
        res = 0
        
        for x in commands:
            
            if x == -2:
                cur -= 1
                cur %= 4
            elif x == -1:
                cur += 1 
                cur %= 4
            else:
                if cur == 0:
                    #scan for block than move to max distance possible
                    idx = bisect_right(xaxis[px], py)
                    nxtblock = float('inf')
                    if idx < len(xaxis[px]):
                        nxtblock = xaxis[px][idx]
                    
                    py = min(nxtblock -1, py + x)
                    
                elif cur == 1:
                    
                    idx = bisect_right(yaxis[py], px)
                    nxtblock = float('inf')
                    if idx < len(yaxis[py]):
                        nxtblock = yaxis[py][idx]
                    
                    px = min(nxtblock -1, px + x)
                    
                elif cur == 2: 
                                 
                    idx = bisect_left(xaxis[px], py)
                    idx -= 1
                    nxtblock = float('-inf')
                    if idx >= 0:
                        nxtblock = xaxis[px][idx]
                    
                    py = max(nxtblock +1, py - x)
                    
                else:
                                        
                    idx = bisect_left(yaxis[py], px)
                    idx -=1
                    nxtblock = float('-inf')
                    if idx >= 0:
                        nxtblock = yaxis[py][idx]
                    
                    px = max(nxtblock + 1, px - x)
                    
                res = max(res, calcE(px,py))
        
        return res
            