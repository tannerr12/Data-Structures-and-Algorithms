class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        
        def calcTotal(x,y):
            total= 0
            for j in range(len(towers)):
                a,b,c = towers[j]
                dist = ((x - a)**2 + (y - b)**2)**0.5
                
                if dist <= radius:
                    total += c // (1 + dist)
                
            return total
        
        ans = [0,0]
        res = 0
        for x in range(51):
            for y in range(51):

                total = calcTotal(x,y)
                if total > res:
                    res = total
                    ans = [x,y]
        

        return ans
        

