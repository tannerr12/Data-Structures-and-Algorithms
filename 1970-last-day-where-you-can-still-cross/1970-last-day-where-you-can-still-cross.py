class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def isGood(mid):
            q = deque()
            
            banned = set()
            for i in range(mid+1):
                x,y = cells[i]
                banned.add((x-1,y-1))
            
            for i in range(col):
                
                if (0,i) not in banned:
                    q.append((0, i))
            
            seen = set()
            directions = [[1,0],[-1,0],[0,-1],[0,1]]
            while q:
                
                for i in range(len(q)):
                    
                    x,y = q.popleft()
                    if (x,y) in seen:
                        continue
                    
                    if x == row - 1:
                        return True
                    seen.add((x,y))
                        
                    for a,b in directions:
                        
                        newx,newy = x + a, y + b
                        
                        if newx >= 0 and newy >= 0 and newx < row and newy < col and (newx,newy) not in banned and (newx,newy) not in seen:
                            
                            q.append((newx,newy))

            return False
                    
                    
                    
        
        grid = [[0 for j in range(col)] for i in range(row)]
        
        l,r = 0, len(cells) -1
        res = 0
        while l <= r:
            
            mid = (l+r) //2
            
            if isGood(mid):
                res = mid +1
                l = mid + 1
            else:
                r = mid -1
                        
            
        return res