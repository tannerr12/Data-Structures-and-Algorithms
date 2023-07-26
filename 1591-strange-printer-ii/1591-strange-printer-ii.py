class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #find ordering
        adj = defaultdict(set)
        indegree = defaultdict(set)
        total = set()
        m,n = len(targetGrid), len(targetGrid[0])
        for i in range(1, 61):
            
            mnX, mnY = float('inf'), float('inf')
            mxX,mxY = 0,0
            for j in range(m):
                for k in range(n):
                    
                    if targetGrid[j][k] == i:
                        mnX = min(mnX, j)
                        mnY = min(mnY, k)
                        mxX = max(mxX, j)
                        mxY = max(mxY, k)
            
            if mnX == float('inf'):
                continue
            total.add(i)
            if i not in adj:
                adj[i] = set()
            if i not in indegree:
                indegree[i] = set()
            for j in range(mnX, mxX + 1):
                for k in range(mnY, mxY + 1):
                    if targetGrid[j][k] != i:
                        adj[i].add(targetGrid[j][k])
                        indegree[targetGrid[j][k]].add(i)
        
        q = deque()
        
        for key in indegree:
            if len(indegree[key]) == 0:
                q.append(key)
            
        res = False
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                if node not in total:
                    continue
                total.remove(node)
                if len(total) == 0:
                    return True
                for key in adj[node]:
                    
                    indegree[key].remove(node)
                    if len(indegree[key]) == 0:
                        q.append(key)
        
        return False
                
                
            
        
        '''
        #print(adj)
        
        memo = {}
        def dfs(mask):
            if mask == fullMask:
                return True
            if mask in memo:
                return memo[mask]
            res = False
            for i in adj:
                if mask & (1 << i) == 0 and fullMask & (1 << i) > 0:
                    process = True
                    for key in adj[i]:
                        if mask & (1 << key) == 0:
                            process = False
                            break
                    if process:
                        res = res or dfs(mask | (1 << i))
            memo[mask] = res
            return res
        
        

        return dfs(0)
        '''