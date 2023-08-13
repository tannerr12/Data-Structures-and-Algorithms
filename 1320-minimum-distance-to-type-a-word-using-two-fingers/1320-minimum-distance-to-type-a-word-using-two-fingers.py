class Solution:
    def minimumDistance(self, word: str) -> int:
        
        
        def distance(x,y):
            r1,c1 = (ord(x) - ord('A')) // 6,(ord(x) - ord('A')) % 6
            r2,c2 = (ord(y) - ord('A')) // 6,(ord(y) - ord('A')) % 6
            return abs(r1 - r2) + abs(c1 - c2) 
            
        
        @cache
        def dfs(i,f1,f2):
            
            if i >= len(word):
                return 0
            
            res = float('inf')
            
            if f1 != '':
                #move finger1
                res = min(res, dfs(i + 1,word[i], f2) + distance(f1,word[i]))
            else:
                res = min(res, dfs(i + 1,word[i], f2))
            if f2 != '':
                #move finger2
                res = min(res, dfs(i + 1,f1, word[i]) + distance(f2,word[i]))
            else:
                res = min(res, dfs(i + 1,f1, word[i]))
            
            
            return res
        
        return dfs(0,'','')