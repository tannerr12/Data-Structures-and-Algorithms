class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n)]
        rank = [0] * n
        
        def find(x):
            
            if x == parent[x]:
                return parent[x]
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            
            px,py = find(x), find(y)
            
            if px == py:
                return True
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                rank[px] += 1
                parent[py] = px
            
            
        
        def isConnected(x,y):
            return find(x) == find(y)
        

            
        
        ans = []
        
        for x,y in requests:
            found = False
            for a,b in restrictions:
                if (isConnected(a,x) and isConnected(b,y)) or (isConnected(b,x) and isConnected(a,y)):
                    found = True
                    break

            if not found:
                union(x,y)
                ans.append(True)
            else:
                ans.append(False)
                
        return ans