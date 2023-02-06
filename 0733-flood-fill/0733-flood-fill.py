class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        n,m = len(image), len(image[0])
        start = image[sr][sc]
        if newColor == start:
            return image
        
        
        q = deque()
        
        q.append((sr,sc))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            
            for i in range(len(q)):
                
                r, c = q.popleft()
                
                image[r][c] = newColor
                for x,y in directions:
                    newx, newy = r + x, c + y
                    
                    if newx < n and newx >= 0 and newy < m and newy >=0 and image[newx][newy] == start:
                        q.append((newx, newy))
        
        return image
                    
                    
                    
                

        