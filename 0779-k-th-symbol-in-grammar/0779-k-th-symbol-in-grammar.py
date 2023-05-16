class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''
        #dp = {1 : '0', 2: '01', 3: '0110'}
        st = '01101001'
        st2 ='10010110'
        
        val = n // 8
       
        if val % 2 == 0:
            return int(st[(k-1)%8])
        else:
            return int(st2[(k-1)%8])
        '''
        '''
        dp = {1 : '0', 2: '01', 3: '0110'}
        for i in range(4, n):
            dp[i] = dp[i-1] + dp[i-1][len(dp[i-1]) // 2:] + dp[i-2]
        
        if n in dp:
            return int(dp[n][k-1])
        
        if k <= len(dp[n-1]):
            return int(dp[n-1][k-1])
        elif k - len(dp[n-1]) <= len(dp[n-1]) // 2:
            return int(dp[n-1][k-1-(len(dp[n-1]) //2)])
        else:
            k -= len(dp[n-1])
            k -= len(dp[n-1])//2
            return int(dp[n-2][k-1])
        '''
        
        
        def dfs(n,k):
            
            if n is 1:
                return 0
        
            parent = dfs(n-1,math.ceil(k/2))
            
            odd = k % 2
            
            if parent == 1:
                return 1 if odd else 0
                
            else:
                return 0 if odd else 1
        
        
        return dfs(n,k)
        
        