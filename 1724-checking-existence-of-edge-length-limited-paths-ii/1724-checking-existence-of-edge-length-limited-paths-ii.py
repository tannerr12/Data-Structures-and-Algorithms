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
    def query(self, p: int, q: int, limit: int) -> bool:
        
        
        if limit > self.mWeight and self.count == 0:
            return True
        else:
            
            if self.isConnected(p,q) == False:
                return False
            return self.dfs(p,q,limit)
    
    #iterative vs recursive dfs seems to be fast enough to pass
    def dfs(self,p,q,limit):
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
        



# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)