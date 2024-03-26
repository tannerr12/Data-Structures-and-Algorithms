class Solution:
    def findIntegers(self, n: int) -> int:
        
        mxDepth = 0
        for i in range(30):
            if n & (1 << i) > 0:
                mxDepth = i
        
        '''
        def dfs(num,depth):
            
            if depth > mxDepth:
                return 1
            last = False
            if depth > 0:
                last = (num & (1 << (depth - 1))) > 0
            res = 0
            
            #add 1
            if not last and (num | (1 << depth)) <= n:
                res += dfs(num | (1 << (depth)), depth + 1) 
            
            #add 0 
            res += dfs(num, depth + 1) 
            
            return res
        
        
        return dfs(0, 0)
        
        '''
        
        #does not account for inbetween numbers
        #answer will fall between -1 and -2
        '''
        dp = [[1,1] for i in range(mxDepth+1)]
        
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
        '''
        #0,1
        #00,01 + 10
        #print(dp)
        #100
        #111
        '''
        @cache
        def dfs(i,under,last):
            
            if i < 0:
                return 1
            
            res = 0
            
            if not last and ((not under and n & (1 << i) > 0) or under):
                res += dfs(i-1, under,True) 
            
            res += dfs(i-1, under == True or n & (1 << i) > 0, False) 
            
            return res
        
        return dfs(mxDepth, False, False)
        '''
    
        
        dp = [[0,1] for i in range(mxDepth+1)]
        
        dpAns = [0 for i in range(mxDepth+1)]
        dpAns[0] = 1
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
            dpAns[i] = dp[i][0] + dp[i][1]
        
        last = 0
        ans = 0
        for i in range(len(dp)-1,-1,-1):
            bit = n & (1 << i) > 0
            
            if bit:
                
                ans += sum(dp[i])
                if last:
                    return ans
        
            last = bit
        
        return ans + 1
                
                