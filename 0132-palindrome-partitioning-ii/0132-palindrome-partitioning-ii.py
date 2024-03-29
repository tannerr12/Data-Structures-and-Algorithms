class Solution:
    def minCut(self, s: str) -> int:
        
        mp = defaultdict(list)
        #gather all palindrone pairs
        
        for i in range(len(s)):
            l,r = i, i+1
            #gather even sized
            while l >= 0 and r < len(s) and s[l] == s[r]:
                mp[l].append(r)
                l -= 1
                r += 1
            
            l, r = i,i
            #gather odd sized
            while l >= 0 and r < len(s) and s[l] == s[r]:
                mp[l].append(r)
                l -= 1
                r += 1            
            
            
        @cache
        def dfs(last):
            
            if last == len(s):
                return 0
            
            res = float('inf')
            
            #cut
            for i in range(len(mp[last])):
                res = min(res,dfs(mp[last][i] + 1) + 1)
                
            
            return res
            
       
        #print(mp)
        return dfs(0) -1
                