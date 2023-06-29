class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        M,N = len(mat), len(mat[0])
        gmask = 0
        pos = 0
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1:
                    gmask |= (1 << pos)
                
                pos +=1
                
        @cache
        def bfs(mask,gridMask):
            nonlocal M,N
            if gridMask == 0:
                return 0
            
            res = float('inf')
            pos = 0
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                     
                    if mask & (1 << pos) > 0:
                        pos +=1
                        continue
                    
                    oldMask = gridMask
                    #update up , down , left , right
                    if pos+1 < M*N and (pos + 1) % N != 0:
                        gridMask ^= (1 << (pos + 1))
                    if pos > 0 and pos % N != 0:
                        gridMask ^= (1 << (pos - 1))
                    if pos - N >= 0:
                        gridMask ^= (1 <<(pos - N))
                    if pos + N < M*N:
                        gridMask ^= (1 << (pos + N))
                    
                    gridMask ^= (1 << pos)
                    
                    res = min(res,bfs(mask | (1 << pos), gridMask) + 1)
                    
                    gridMask = oldMask
                    pos +=1
            
            
            return res
        
        ans = bfs(0, gmask)
        
        return ans if ans != float('inf') else -1
            
            
            
        
