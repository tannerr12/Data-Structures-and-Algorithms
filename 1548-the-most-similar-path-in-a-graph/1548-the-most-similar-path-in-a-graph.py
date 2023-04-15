class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for x,y in roads:
            
            adj[x].append(y)
            adj[y].append(x)
            
        INF = 10 ** 20
        P = len(targetPath)
            
        choice = [[None] * n for _ in range(P)]
        cache = [[None] * n for _ in range(P)]
        has_cache = [[None] * n for _ in range(P)]
        
        def dfs(index,current):
            delta = 0
            
            if names[current] != targetPath[index]:
                delta = 1
            
            if index == P-1:
                return delta
            
            if has_cache[index][current]:
                return cache[index][current]
            
            res = INF
            
            for val in adj[current]:
                
                score = dfs(index + 1, val) + delta
                
                if score < res:
                    choice[index][current] = val
                    res = score

            has_cache[index][current] = True
            cache[index][current] = res
            
            return res 
        
        best = float('inf')
        first = None
        for i in range(n):
            score = dfs(0,i)
            if score < best:
                first = i
                best = score
        
        
        print(choice)
        #our depth
        cs = 0
        #what node are we on
        cn = first
        #our path
        rs = []
        
        while cn is not None:
            rs.append(cn)
            
            cn = choice[cs][cn]
            cs +=1
        
        return rs
        
       
        
        