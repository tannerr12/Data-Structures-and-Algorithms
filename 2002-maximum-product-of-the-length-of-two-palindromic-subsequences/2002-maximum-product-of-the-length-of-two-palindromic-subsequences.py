class Solution:
    def maxProduct(self, s: str) -> int:
        #idea can we use 26 bits and for each bit position = character palindrone = 0 non = 1 if prev palindrone and new len odd = palindrone if even bits = 0
        
        def isPalindrone(s):
            
            l,r = 0, len(s) -1
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            
            return True
                
        @cache
        def dfs(i,l,r):
            
            if i >= len(s):
                if isPalindrone(l) and isPalindrone(r):
                    return len(l) * len(r)
                return 0
                        
            res = 0
            
  
            #left
            res = max(res,dfs(i+1, l+s[i], r))
            #right
            res = max(res,dfs(i+1, l,r+s[i]))

            #None
            res = max(res, dfs(i+1,l,r))
                
            return res
        
        
        
        return dfs(0,'','')
                
        