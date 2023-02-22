class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parent = [i for i in range(len(wells) + 1)]
        rank = [1] * (len(wells) + 1)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        def union(x,y):
            
            val1 = find(x)
            val2 = find(y)
            
            if val1 != val2:
                
                #they are not the same
                if rank[val1] > rank[val2]:
                    parent[val2] = val1
                elif rank[val2] > rank[val1]:
                    parent[val1] = val2
                
                else:
                    parent[val2] = val1
                    rank[val1] +=1
                
                return True
            return False
        
        def Connected(x,y):
            return find(x) == find(y)
        
        
        arr = []
        #connect all the wells house 0 to other houses
        for i in range(len(wells)):
            arr.append((wells[i], 0, i+1))
            
        for h1,h2,cost in pipes:
            arr.append((cost,h1,h2))
        
        arr.sort()
        res = 0
        for cost,h1,h2 in arr:
            if union(h1,h2):
                res += cost
        return res
            
        
        