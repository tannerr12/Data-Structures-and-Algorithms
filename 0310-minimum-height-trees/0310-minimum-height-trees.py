class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        adj = defaultdict(list)
        adjInd = defaultdict(int)
        for x,y in edges:
            adj[x].append(y)
            adjInd[x]+=1
            adj[y].append(x)
            adjInd[y]+=1
            
        res = []
        size = n
        
        q = deque()
        for i in range(n):
            
            if adjInd[i] == 1:
                q.append(i)
        
        
        while size > 2:
            
            size -= len(q)
            for j in range(len(q)):
                node = q.popleft()
                
                for x in adj[node]:
                    adjInd[x] -=1
                    
                    if adjInd[x] == 1:
                        q.append(x)
        
        #print(q)
        
        return q
        
        
        
        