class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        ans = []
        
        @cache
        def dfs(i,j):
            
            if i >= len(str1) and j >= len(str2):
                return 0
            
            res = float('inf')

            if i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                #advance both (they are the same)
                res = min(res, dfs(i+1,j+1) + 1)
            else:    
                if i < len(str1):
                    #advance i
                    res = min(res, dfs(i+1, j) + 1)
                if j < len(str2):
                    #advance j
                    res = min(res, dfs(i, j+1) + 1)
            
            
            return res
        
        
        q = deque([[0,0,'']])
        seen = set()
        while q:
            
            for i in range(len(q)):
                
                i,j,path = q.popleft()
                if (i,j) in seen:
                    continue
                seen.add((i,j))
                if i >= len(str1) and j >= len(str2):
                    return path
                
                if i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                    q.append([i+1,j+1,path + str1[i]])
                else:
                    if i < len(str1):
                        q.append([i+1, j, path + str1[i]])
                    if j < len(str2):
                        q.append([i, j + 1, path + str2[j]])
                    