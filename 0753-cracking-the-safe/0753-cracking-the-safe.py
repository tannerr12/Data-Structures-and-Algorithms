class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        '''  
        q = deque([('', set())])
        gl = set()
        while q:
            
            for i in range(len(q)):
                
                node,vals = q.popleft()
                
                if len(vals) > 0 and vals in gl:
                    continue

                if len(node) >= n:
                    vals.add(node[-n:])
                if len(vals) > 0:
                    gl.add(frozenset(vals))                
                if len(vals) == k ** n:
                    return node
                
        
                for j in range(k):
                    q.append((node + str(j),vals.copy()))
        
        
                    
        '''
        vals = set()
        ans = ''
        vals.add('0' * n)
        @cache
        def dfs(s):
            nonlocal ans
            
            if ans:
                return True
            
            if len(vals) == k ** n:
                ans = s
                return True
            
            for v in range(k):
                ns = s + str(v)
                if ns[-n:] not in vals:
                    vals.add(ns[-n:])
                    if dfs(ns):
                        vals.remove(ns[-n:]) 
                        return True
                    vals.remove(ns[-n:])    
                    
        dfs('0' * n)
        
        return ans