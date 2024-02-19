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
            
        for key,val in mp.items():
            mp[key].sort()
        
            
        @cache
        def dfs(i,last):
            
            if last == len(s):
                return 0
            
            res = float('inf')
            
            #cut
            if i < len(mp[last]):
                res = min(res,dfs(0, mp[last][i] + 1) + 1)
                #skip
                res = min(res, dfs(i+1, last))
            
            return res
            
       
        #print(mp)
        return dfs(0,0) -1
                