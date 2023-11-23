class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            nonlocal st,idVal
            stack.append(i)
            inStack[i] = True
            lowLink[i] = idVal
            ids[i] = idVal
            idVal += 1
            
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 0 or i == j:
                    continue
                    
                if ids[j] == -1:
                    dfs(j)
                
                if inStack[j]:
                    lowLink[i] = min(lowLink[i], lowLink[j])
            
            if lowLink[i] == ids[i]:
                
                while stack:
    
                    val = stack.pop()
                    inStack[val] = False 
                    lowLink[val] = ids[i]
                    if val == i:
                        break

                st += 1
        
        n = len(isConnected)
        st = 0
        stack = []
        inStack = [False] * n
        lowLink = [-1] * n
        ids = [-1] * len(isConnected)
        idVal = 0
        
        for i in range(len(isConnected)):
            
            if ids[i] == -1:
                dfs(i)
            
            
        
        return st
        
        
        