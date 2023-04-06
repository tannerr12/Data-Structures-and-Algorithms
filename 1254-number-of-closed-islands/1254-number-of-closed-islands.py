class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        parent= {}
        rank = defaultdict(int)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
            
        def union(x,y):
            
            v1,v2 = find(x), find(y)
            
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                    
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                
                
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        n,m = len(grid), len(grid[0])
        invalid = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                if (i,j) not in parent:
                    parent[(i,j)] = (i,j)    
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    invalid.add((i,j))
                if i + 1 < n and grid[i+1][j] == grid[i][j]:
                    if i + 1 == n-1:
                        invalid.add((i+1,j))
                    if (i+1, j) not in parent:
                        parent[(i+1,j)] = (i+1,j)
                    union((i,j), (i+1,j))
                        
                
                if j + 1 < m and grid[i][j+1] == grid[i][j]:
                    if j+1 == m-1:
                        invalid.add((i,j+1))
                    if (i, j + 1) not in parent:
                        parent[(i,j+1)] = (i,j+1)
                    union((i,j), (i,j+1))
        
        
        uni = set()
        inv = 0
        
        for key in parent:
            uni.add(find(key))
         
        #print(uni)
        #print(invalid)
        for key in uni:
            for val in invalid:
                if isConnected(key,val):
                    inv +=1
                    break
        
        return len(uni) - inv
            
        