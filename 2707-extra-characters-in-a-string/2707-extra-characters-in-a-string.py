class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictMp = defaultdict(list)
        
        for word in dictionary:
            dictMp[word[0]].append(word)
        
       
        
        @cache
        def dfs(i):
            
            if i >= len(s):
                return 0
            
            res = float('inf')
            #skip letter add 1 to cost
            res = min(res, dfs(i+1) + 1)
            
            for word in dictMp[s[i]]:
                if s[i:i+len(word)] == word:
                    res = min(res,dfs(i+len(word)))
            
            
            return res
        
        return dfs(0)
                