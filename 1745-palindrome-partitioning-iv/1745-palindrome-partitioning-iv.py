class Solution:
    def checkPartitioning(self, s: str) -> bool:
        
        
        palis = defaultdict(list)
        
        for i in range(len(s)):
            
            l,r = i,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palis[l].append(r)
                l-=1
                r+=1
            
            
            l,r = i-1,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palis[l].append(r)
                l-=1
                r+=1
        
        
        
        #print(palis)
        
        @cache
        def dfs(i,count):
            
            if i >= len(s) and count == 3:
                return True
            elif count == 3 or i >= len(s):
                return False
            
            res = False
            for val in palis[i]:
                res = res or dfs(val + 1,count + 1)
                
            
            return res
        
        
        
        return dfs(0,0)