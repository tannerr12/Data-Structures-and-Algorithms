class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        '''
        @cache
        def dfs(i, changed):
            
            if i >= len(word):
                return 0
            
            res = float('inf')
            #change
            res = min(res, dfs(i+1, True) + 1)
            
            #dont change
            if changed or abs(ord(word[i]) - ord(word[i-1])) > 1:
                res = min(res, dfs(i+1, False))
                
            
            return res
        
        return dfs(0,True)
        '''
        
        res = 0
        prev = False
        for i in range(1, len(word)):
            
            if not prev and abs(ord(word[i]) - ord(word[i-1])) <= 1:
                prev = True
                res += 1
            
            else:
                prev = False
        
        return res
            
            
            