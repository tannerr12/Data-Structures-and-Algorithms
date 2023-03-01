class DistanceLimitedPathsExist:
    
    
    def find(self,val):
        
        
        if val == self.parent[val]:
            return val

        self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def union(self,x,y):
        
        v1,v2 = self.find(x),self.find(y)
        
        if v1 != v2:
            
            if self.rank[v1] > self.rank[v2]:
                self.parent[v2] = v1
            
            elif self.rank[v2] > self.rank[v1]:
                self.parent[v1] = v2
                
            else:
                self.parent[v2] = v1
                self.rank[v1] +=1
            return True
        return False
    
    def isConnected(self,x,y):
        
        return self.find(x) == self.find(y)
            
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.edges = sorted(edgeList, key=lambda x: (x[2]))
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.n = n
        self.count = n -1
        self.mWeight = 0
        self.adj = defaultdict(list)
        
        for x,y,weight in self.edges:
            if self.union(x,y):
                self.mWeight += weight
                self.count -=1
            self.adj[x].append((y,weight))
            self.adj[y].append((x,weight))
       # print(self.wMap)
    def query(self, p: int, q: int, limit: int) -> bool:
        
        
        if limit > self.mWeight and self.count == 0:
            return True
        else:
            
            if self.isConnected(p,q) == False:
                return False
            
            return self.dfs2(p,q,limit)
    
    
    def dfs2(self,p,q,limit):
            i = 0
            stack = [p]
            seen = set()
            while stack:
                curr = stack.pop()
                if curr == q:
                    return True
                seen.add(curr)
                nei = []
                for i,w in self.adj[curr]:

                    if w < limit and not (i in seen):
                        stack.append(i)
            return False
        
        
        
  
    @cache
    def findMap(self,val,target,limit):
        
        if val == target:
            return True
        self.seen.add(val)
        res = False
        
        for key,v in self.wMap[val].items():
            if v >= limit or key in self.seen:
                continue
            res = res or self.findMap(key,target,limit)
        
        return res
    """          
    def execute(self,p,q,limit):
        self.parent = [i for i in range(self.n)]
        self.rank = [0] * self.n
        self.count = self.n-1
        for x,y,weight in self.edges:
            if weight >= limit:
                break
            
            if self.union(x,y):
                self.count -=1
            
            
            if self.count == 0:
                break

        if self.isConnected(p,q):
            return True
        return False
     """ 


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)