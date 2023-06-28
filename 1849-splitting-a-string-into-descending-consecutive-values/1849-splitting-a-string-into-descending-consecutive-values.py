class Solution:
    def splitString(self, s: str) -> bool:
        al = int(s)
        
        @cache
        def dfs(i,last):
            nonlocal al
            if i >= len(s):
                return last != al
            
            res = False
            for j in range(i, len(s)):
                v = int(s[i:j+1])
                if v < last:
                    if abs(last - v) == 1 or last == float('inf'):
                        res = res or dfs(j + 1, int(s[i:j+1]))
                else:
                    break
            
            return res
        
        
        return dfs(0,float('inf'))
            
            