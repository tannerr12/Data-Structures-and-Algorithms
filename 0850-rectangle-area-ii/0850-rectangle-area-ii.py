class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10**9 + 7
        
        points = []
        
        
        def getArea(width):
            total = 0
            prevbot = 0
            for bot,top in intervals:
                bot = max(bot,prevbot)
                
                if top > bot:
                    total += (top - bot) * width
                    prevbot = top
            
            return total
                
        
        for x1,y1,x2,y2 in rectangles:    
            points.append((x1, 0, y1, y2))
            points.append((x2, 1, y1, y2))
        
        
        points.sort()
        intervals = []
        res = 0
        prev = 0
        for x, typ, y1, y2 in points:
            res += getArea(x - prev)
            
            if typ == 1:
                intervals.remove((y1,y2))
            else:
                intervals.append((y1,y2))
                intervals.sort()

            prev = x
            
        
        return res % mod
        
        