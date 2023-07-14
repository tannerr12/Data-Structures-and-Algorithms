class Solution:
    def minimumDeletions(self, s: str) -> int:
        '''
        dp = [[0,0] for j in range(len(s))]
        
        #print(dp)
        res 
        for i in range(1,len(s)):
            
            #A -> A
            if s[i] == 'a':
                dp[i][0] = dp[i-1][0]    
            #A -> B
            if s[i] == 'b':
                
            #B-> B
            if s[i] == 'b':
            #B -> A
            if s[i] == 'a':
            
        '''
        
        prefixA = []
        prefixB = []
        prefixA.append(0)
        prefixB.append(0)
        
        for i in range(len(s)):
        
            prefixA.append(prefixA[-1] + (s[i] == 'a'))
            prefixB.append(prefixB[-1] + (s[i] == 'b'))
            
        
        
        #print(prefixA)
        
        res = float('inf')
        
        for i in range(len(s)):
            left = prefixB[i]
            right = prefixA[-1] - prefixA[i+1]
            
            res = min(res, left + right)
            
        return res
            