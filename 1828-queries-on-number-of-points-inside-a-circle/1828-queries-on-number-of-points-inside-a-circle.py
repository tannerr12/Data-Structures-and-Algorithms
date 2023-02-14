class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x,y,z in queries:
            
            p = 0
            for a,b in points:
                if sqrt(abs(x-a)**2 + abs(y-b) **2) <= z:
                    p+=1
        
        
            
            res.append(p)
        
        
        return res