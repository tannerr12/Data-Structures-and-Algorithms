class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        mp = defaultdict(list)
        for i in range(len(words)):
    
            for j in range(i+1, len(words)):
                if len(words[i]) != len(words[j]) or groups[j] == groups[i]:
                    continue
                    
                dist = 0
                for k in range(len(words[i])):
                    
                    if words[i][k] != words[j][k]:
                        dist +=1
                
                if dist == 1:
                    mp[i].append(j)
        
        #print(mp)
        
        @cache
        def dfs(cur):
            
            ans = 0
            
            for val in mp[cur]:
                
                ans = max(ans, dfs(val) + 1)
            
            
            return ans
        
        best = 0
        start = 0
        for i in range(len(words)):
            val = dfs(i) + 1
            
            if val > best:
                best = val    
                start = i
                
        
        #print(best)
        ans = []
        ans.append(start)
        fans = ans.copy()
        @cache
        def dfs2(i,score):
            nonlocal best,fans
            
            if score == best:
                fans = ans.copy()
                return
            if len(fans) > 1:
                return
           
            
            for val in mp[i]:
                ans.append(val)
                dfs2(val,score + 1)
                ans.pop()
            

            
            return 
        
        dfs2(start,1)
        
        for i in range(len(fans)):
            fans[i] = words[fans[i]]
        return fans
                
            
        