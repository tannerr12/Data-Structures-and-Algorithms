class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        
       
        def checkArr(c):
            mn = float('inf')
            mx = float('-inf')
            for val in c.values():
                if val > 0:
                    mn = min(mn, val)
                    mx = max(mx, val)
            
            return mn == mx or mn == float('inf')
        
        @cache
        def dfs(i):

            if i >= len(s):
                return 0
            
            count = defaultdict(int)
            ans = float('inf')
            for j in range(i, len(s)):
                #char = ord(s[j]) - ord('a')
                count[s[j]] += 1
  
                if len(set(count.values())) == 1:
                    ans = min(ans, dfs(j+1) + 1)
                    
            return ans
        
        
        
        return dfs(0)