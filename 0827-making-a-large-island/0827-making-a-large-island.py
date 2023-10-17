class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        '''
        [1,0,1,0,1],
        [0,1,1,0,1],
        [1,1,1,0,0],
        [1,0,1,1,1],
        [0,0,1,1,0]]
        '''
        
        rank = defaultdict(int)
        parent = defaultdict(tuple)
        size = defaultdict(int)
        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                x = find(parent[x])
            
            return x
        
        
        def union(x,y):
            
            parx = find(x)
            pary = find(y)
            
            if parx != pary:
                
                if rank[parx] > rank[pary]:
                    parent[pary] = parx
                    size[parx] += size[pary]
                    del size[pary]
                elif rank[pary] > rank[parx]:
                    parent[parx] = pary
                    size[pary] += size[parx]
                    del size[parx]
                    
                else:
                    rank[parx] += 1
                    parent[pary] = parx
                    size[parx] += size[pary]
                return True
            return False
        #1 0
        #0 1
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    size[(i,j)] = 1
                    if i > 0 and grid[i-1][j] == 1:
                        union((i,j), (i-1,j))
                    if j > 0 and grid[i][j-1] == 1:
                        union((i,j), (i,j-1))
        
        #print(parent)
        #print(size)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    temp = 1
                    parSeen = set()
                    if i > 0 and grid[i-1][j] == 1:
                        par = find((i-1,j))
                        temp += size[par]
                        parSeen.add(par)
                    if j > 0 and grid[i][j-1] == 1:
                        par = find((i,j-1))
                        if par not in parSeen:
                            parSeen.add(par)
                            temp += size[par]
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        par = find((i+1,j))
                     
                        if par not in parSeen:
                            parSeen.add(par)
                            temp += size[par]
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        par = find((i,j+1))
                        if par not in parSeen:
                            temp += size[par]
                    
                    res = max(res, temp)
        
        
        for key,val in size.items():
            res = max(res, val)
        
        return res