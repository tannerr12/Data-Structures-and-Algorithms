class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        n,m = len(image), len(image[0])
        start = image[sr][sc]
        if newColor == start:
            return image
        
    
        def dfs(r,c,start):
            
            if r >= n or r < 0 or c >= m or c < 0 or image[r][c] != start:
                return 0
            
            image[r][c] = newColor
            
            #check 4 directions
            
            dfs(r+1,c,start)
            dfs(r-1,c,start)
            dfs(r,c+1,start)
            dfs(r,c-1,start)
            
            
            
        
        dfs(sr,sc,start)
        
        return image

        