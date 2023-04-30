class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n+1)]
        rank = [0] * (n + 1)
        count = n-1
        def find(val):
            if val == parent[val]:
                return val
            parent[val] = find(parent[val])
            return parent[val]

        def union(x,y):
            nonlocal count
            v1,v2 = find(x),find(y)
            if v1 != v2:
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                count -=1
                return False
            
            return True

        def isConnected(x,y):
            return find(x) == find(y) 
        
        
        res = 0
        for t,x,y in edges:
            if t == 3:
                if union(x,y):
                    res +=1

        p = parent.copy()
        r = rank.copy()
        c = count
        for t,x,y in edges:
            if t == 1:
                if union(x,y):
                    res += 1 
        
        if count != 0:
            return -1
        parent = p
        rank = r
        count = c
        for t,x,y in edges:
            if t == 2: 
                if union(x,y):
                    res += 1
            
        if count != 0:
            return -1
        return res