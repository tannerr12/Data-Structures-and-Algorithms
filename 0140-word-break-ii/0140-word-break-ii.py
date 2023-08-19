class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)
        @cache
        def dfs(i,st,last):
            
            if i >= len(s):
                if last == i-1:
                    ans.append(st[:-1])
                return 
            
            
            #take character
            dfs(i+1, st + s[i], last)
            #take word
            if s[last+1:i+1] in wordDict:
                dfs(i+1, st + s[i] + ' ', i)
        
        
        dfs(0,'',-1)
        
        print(ans)
        return ans