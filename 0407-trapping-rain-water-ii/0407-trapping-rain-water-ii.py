class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        heap = []
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or i == len(heightMap)-1 or j == 0 or j == len(heightMap[0]) -1:
                    heappush(heap,[heightMap[i][j], i,j])
                    heightMap[i][j] = -1
                    
        res = 0
        while heap:
            
            val, i,j = heappop(heap)
            
            for x,y in directions:
                nx = x + i
                ny = y + j
                if nx >= len(heightMap) or nx < 0 or ny >= len(heightMap[0]) or ny < 0 or heightMap[nx][ny] == -1:
                    continue
            
                res += max(0, val - heightMap[nx][ny])
                
                heappush(heap, [max(heightMap[nx][ny], val), nx,ny])
                
                heightMap[nx][ny] = -1
                
            
            
        
        
        return res
                