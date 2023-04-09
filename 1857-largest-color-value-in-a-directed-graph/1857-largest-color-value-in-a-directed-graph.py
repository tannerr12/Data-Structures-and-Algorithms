class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        #start from each leaf
        #keep track of largest color count and update res
        #use a seen list to detect cycles in the graph
        adj = defaultdict(list)
        leafs = set([i for i in range(len(colors))])
        for x,y in edges:
            if x == y:
                return -1
            adj[x].append(y)
            if y in leafs:
                leafs.remove(y)
        
        
        seen = defaultdict(dict)
        cycle = set()
        cyc = False
        
        
        def dfs(i):
            nonlocal cyc
            if i in cycle:
                cyc = True
                return {}
            if i in seen:
                return seen[i]
            
            cycle.add(i)
            
            if colors[i] in seen[i]:
                seen[i][colors[i]] += 1
            else:
                seen[i][colors[i]] = 1
                
            temp = defaultdict(int)
            for x in adj[i]:
      
                arr = dfs(x)
                
                for key,val in arr.items():
                    temp[key] = max(temp[key], val)
            
            for key,val in temp.items():
                if key in seen[i]:
                    seen[i][key] += val
                else:
                    seen[i][key] = val
            
            
            cycle.remove(i)
                
            return seen[i]
                
            
        res = 0
        
        if len(leafs) == 0:
            return -1
        #find leafs
        for val in leafs:
            
            dfs(val)
            res = max(res,max(seen[val].values()))
            cycle = set()
            if cyc:
                return -1
        
        
        return res if len(seen) == len(colors) else -1
            
            