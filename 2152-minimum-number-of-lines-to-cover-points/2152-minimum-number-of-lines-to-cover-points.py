from math import atan2, degrees, radians

class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        #store all possible line angles 
        #go through each line possiblity?
        if len(points) <= 2:
            return 1
        
        n, line_points= len(points), defaultdict(set)
        
        
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1):
                x2,y2 = points[j]
                if x1 == x2:
                    a,b = x1, sys.maxsize
                else:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                line_points[(a,b)].add((x1,y1))
                line_points[(a,b)].add((x2,y2))
        
        lines = [line for line,points in line_points.items() if len(points) > 2]
        
        ans, m = math.ceil(n/2), len(lines)
        
        
        for i in range(1, 2 ** m):
            #count the number of on bits 
            j,cnt = 0, bin(i).count('1')
            cur_points = set()
            
            while i > 0:
                if i % 2:
                    cur_points |= line_points[lines[m-1-j]]
                i >>=1
                j +=1
            ans = min(ans, cnt + math.ceil((n-len(cur_points)) /2))
        
        return ans
        """
        @cache
        def backtrack(i,bitmask):
            
            if i >= len(points):
                
                return len(h.keys())
            
            source = points[i]
            res = float('inf')
            for j in range(len(points)):
                if i == j: 
                    continue
                if bitmask & (1 << j) == 0:
                    dest = points[j]
                    angle = 0
                    if dest[0] - source[0] == 0:
                        angle = math.inf
                    
                    else:
                        angle = (dest[1] - source[1]) / (dest[0] - source[0])
                    angle = abs(angle)
                    if angle not in h:
                        h[angle] = []
                    h[angle].append(dest)
                    res = min(res,backtrack(i+1,bitmask | (1 << j)))
                    h[angle].pop()
                    if len(h[angle]) == 0:
                        del h[angle]
            
            return res
                    
        
        
        return backtrack(0,0)
        
        """
