class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #create an adjacency list between the bombs first than we will run dfs on all of the bombs and pick the bomb with the largest adjacency list
        #we want to add all adjacency instead of finding the longest path
        
        adj = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                                
                b1 = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
                
                if b1 <= r1:
                    adj[i].append(j)
                if b1 <= r2:
                    adj[j].append(i)
        
      
        
        def dfs(i):
            
            if i in seen:
                return 0
            
            seen.add(i)
            res = 0
            for val in adj[i]:
                
                if val in seen:
                    continue
                res += 1 + dfs(val)
            
            return res
        
        res = 1
        seen = set()
        for i in range(len(bombs)):
            
            res = max(res,dfs(i) + 1)
            seen = set()
        
        
        return res
                
                
                