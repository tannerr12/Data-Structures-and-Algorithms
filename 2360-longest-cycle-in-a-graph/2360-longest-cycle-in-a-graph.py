class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        #a cycle node must have atleast 1 indegree and 1 outdegree
        
        adj = defaultdict(list)
        
        #possibly skip ones with no indegree or missing an outdegree and union find through each connection if it doesnt lead back
        #to itself there is no loop but if it does than we update res = max(res,curr)
        #while traversing if we see a node we already used in the future we know its already been checked
        
        invalid = set()
        
        count = defaultdict(int)
        for i,v in enumerate(edges):
            if v == -1:
                invalid.add(i)
                continue
            adj[i].append(v)
            count[i] += 1
            count[v] += 1
        
        
        #print(count)
        
        for key,val in count.items():
            if val <= 1:
                invalid.add(key)
                
        
        
        parent = [i for i in range(len(edges))]
        rank = [0] * len(edges)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
            if v1 != v2:
                
                if rank[v1]> rank[v2]:
                    parent[v2]= v1
                
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                
                return False
            return True
        
        res = 0
        gseen = set()
        for i,val in enumerate(edges):
            idx = i
            count = 0
            valid = False
            seen = {}
            while idx not in invalid and idx not in gseen:
                seen[idx] = count
              #  if union(edges[idx], idx):
              #      valid = True
              #      break
                idx = edges[idx]
                count +=1
                if idx in seen:
                    count = count - seen[idx]
                    valid = True
                    break
                
            
            if valid:
                for key in seen:
                    gseen.add(key)
                res = max(res,count)
        
        
        return res if res > 0 else -1