class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        '''
        st = set()
        
        for i in range(len(s)):
            
            #odd size
            l,r = i,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:    
                st.add(s[l:r+1])
                l-=1
                r+=1
            
            #even size
            l,r = i - 1,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                st.add(s[l:r+1])
                l-=1
                r+=1
        
        
        print(st)
        return len(st)
        '''
        nxt = [[-1 for i in range(4)] for j in range(len(s) + 1)]
        bck = [[-1 for i in range(4)] for j in range(len(s) + 1)]
        #var = -1
        for i in range(len(s)):
            
            for j in range(len(bck[i-1])):
                bck[i][j] = bck[i-1][j]
                
            if i > 0:
                var = ord(s[i-1]) - ord('a')
                bck[i][var] = i -1
            
            
        
      
        for i in range(len(s)-1,-1,-1):
            
            
            for j in range(len(nxt[i+1])):
                nxt[i][j] = nxt[i+1][j]
            if i + 1 < len(s):
                var = ord(s[i+1]) - ord('a')
                nxt[i][var] = i + 1 
            
            
       
    
                
        first = [-1 for j in range(4)]
        last = [-1 for j in range(4)]
        
        for i in range(len(s)):
            var = ord(s[i]) - ord('a')
            
            if first[var] == -1:
                first[var] = i
            
            last[var] = i
        MOD = 10 ** 9 + 7

        
        characters = ['a','b','c','d']
        if len(s) == 1:
            return 1
        
        
        @cache
        def dfs(i,j):
            
            if j <= i:
                return 0
            
            res = 0
            
            #jump to the next matching character
            #also account for skipping the current character
            
            #4 possible jumps
            count = 0
            for k in range(4):
                if nxt[i][k] != -1 and bck[j][k] != -1 and (nxt[i][k] != j and bck[j][k] != i and nxt[i][k] <= bck[j][k]):
                    
                    res += dfs(nxt[i][k], bck[j][k]) + 1
                    if nxt[i][k] != bck[j][k]:
                        res += 1
                    res %= MOD
                    
                    
            
            return res 
        
        
        res = 0
        count = 0
        
        for i in range(4):
            
            if first[i] != -1:
                res += dfs(first[i], last[i]) + 1
                if first[i] != last[i]:
                    res += 1
                res %= MOD
                
        return res % MOD
        
            
            
            
            