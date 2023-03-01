class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(val):
            
            if val == parent[val]:
                return val

            parent[val] = find(parent[val])
            return parent[val]

        def union(x,y):

            v1,v2 = find(x),find(y)

            if v1 != v2:

                if rank[v1] > rank[v2]:
                    parent[v2] = v1

                elif rank[v2] > rank[v1]:
                    parent[v1] = v2

                else:
                    parent[v2] = v1
                    rank[v1] +=1
                return True
            return False

        def isConnected(x,y):

            return find(x) == find(y)
      
        parent = [i for i in range(n)]
        rank = [0] * n
        
        edgeList.sort(key=lambda x: x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        
        queries = sorted(queries, key=lambda x: x[2])
        
        res = [False] * len(queries)
        
        edgeidx = 0
        edgelen = len(edgeList)
        for p,q,limit,i in queries:
            while edgeidx < edgelen and edgeList[edgeidx][2] < limit:
                union(edgeList[edgeidx][0], edgeList[edgeidx][1])
                edgeidx +=1
            
            res[i] = isConnected(p,q)
        
        return res  
    