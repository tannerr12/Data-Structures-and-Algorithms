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
        vals = defaultdict(int)
        ans = []
        vals['0' * n] += 1
        @cache
        def dfs(s):
                        
            if len(vals) == k ** n:
                ans.append(s)
                return True
            
            for v in range(k):
                ns = s + str(v)
                if len(ns) >= n:
                    if vals[ns[-n:]] >= 1:
                        continue
                    vals[ns[-n:]] += 1
                if dfs(ns):
                    return True
            
                if len(ns) >= n:
                    vals[ns[-n:]] -= 1
                    if vals[ns[-n:]] == 0:
                        del vals[ns[-n:]]
        
        
        dfs('0' * n)
        
  
        ans.sort(key=lambda x: (len(x)))
        return ans[0]