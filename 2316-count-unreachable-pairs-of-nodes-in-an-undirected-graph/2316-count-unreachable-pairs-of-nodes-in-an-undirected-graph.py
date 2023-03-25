class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(p):
            
            while parent[p] != parent[parent[p]]:
                parent[p] = parent[parent[p]]
            return parent[p]
        
        def union(v1,v2):
            
            p1 = find(v1)
            
            p2 = find(v2)
            
            if v2 < v1:
                parent[p1] = parent[p2]
            else:
                parent[p2] = parent[p1]
            
            return parent[p2]
        
        
        for x,y in edges:
            
            union(x,y)
            
        for i in range(len(parent)):
            find(i)
        
        h = Counter(parent)
        #print(parent)
        #print(h)
        
        arr = []
        
        for key in h:
            arr.append(key)
        
        
        res = 0
        seen = 0
        for i in range(len(arr)):
            
            res += (n - h[arr[i]] - seen) * h[arr[i]]
    
            seen += h[arr[i]]
            
            
            
        
        
        return res
            