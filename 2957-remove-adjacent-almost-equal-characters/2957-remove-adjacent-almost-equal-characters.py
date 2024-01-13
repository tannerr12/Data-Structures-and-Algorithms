class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        @cache
        def dfs(i, changed):
            
            if i >= len(word):
                return 0
            
            res = float('inf')
            #change
            res = min(res, dfs(i+1, True) + 1)
            
            #dont change
            if i == 0 or changed or abs(ord(word[i]) - ord(word[i-1])) > 1:
                res = min(res, dfs(i+1, False))
                
            
            return res
        
        return dfs(0,False)