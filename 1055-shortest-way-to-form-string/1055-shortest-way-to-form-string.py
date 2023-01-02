class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        vals = set(target)
        valss = set(source)
        
        for key in vals:
            if key not in valss:
                return -1
        
        s = ''
        for w in source:
            if w in vals:
                s += w
        
        
        #print(s)
        
        @cache
        def dfs(i,j,c):
            nonlocal s
            if j >= len(target):
                return c
            
            res = float('inf')
            if i >= len(s):
                res = min(res,dfs(0,j,c+1))
            elif s[i] == target[j]:
                res = min(res,dfs(i+1,j+1,c))
            else:
                res = min(res,dfs(i+1,j,c))

            return res
        
        
        res = dfs(0,0,1)
        
        if res == float('inf'):
            return -1
        return res
            
            