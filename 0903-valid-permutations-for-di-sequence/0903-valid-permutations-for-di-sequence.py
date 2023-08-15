class Solution:
    def numPermsDISequence(self, s: str) -> int:
        
        '''
        class Solution:
    def numPermsDISequence(self, S: str) -> int:
        N = len(S)
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(i, less, more):
            res = 0
            if(i < 0): return 1
            if(less + more == 0): return 0
            if(S[i] == 'I'):
                for k in range(less):
                    res = (res + dp(i-1, k, less - k -1 + more)) % MOD
            elif(S[i] == 'D'):
                for k in range(more):
                    res = (res + dp(i-1, less + k, more - k - 1)) % MOD
            return res
        
        return sum(dp(N-1, k, N-k) for k in range(N+1)) % MOD
        
        
        
        '''
        
        
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i,u,d):
            
            if i < 0:
                return 1
            if d + u == 0:
                return 0
            
            res = 0
            #go up
            if s[i] == 'I':
                for k in range(d):
                    res += dfs(i-1, d - k - 1 + u, k) % MOD
            
                res %= MOD
            #go down
            else:
                for k in range(u):
                    res += dfs(i-1, u - k - 1, d + k) % MOD
                    
                
            res %= MOD
            
            return res
        
        
        u = s.count('I')
        d = s.count('D')
    
    
        ans = 0
        n  = len(s)
        for i in range(n + 1):
            ans += dfs(n - 1, n - i, i) % MOD
        
        
        return ans % MOD