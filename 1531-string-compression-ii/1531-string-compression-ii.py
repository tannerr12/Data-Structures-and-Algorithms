class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache
        def dfs(i, cur, count, rem):
            
            if i >= len(s):
                if count == 0:
                    return 0
                elif count == 1:
                    return 1
                elif count < 10:
                    return 2
                elif count < 100:
                    return 3
                else:
                    return 4
            
            res = float('inf')
            #add to compress
            
            if cur == s[i] or cur == '':
                res = min(res, dfs(i+1, s[i], count + 1, rem))
            
            #reset
            else:
                if count == 1:
                    res = min(res, dfs(i+1,s[i], 1, rem) + 1)
                elif count < 10:
                    res = min(res, dfs(i+1, s[i], 1, rem) + 2)
                elif count < 100:
                    res = min(res, dfs(i+1,s[i], 1, rem) + 3)
                else:
                    res = min(res, dfs(i+1,s[i], 1, rem) + 4)
            if rem:
                #skip
                res = min(res, dfs(i+1, cur, count, rem - 1))
            
            
            return res
    
        
        return dfs(0, '', 0, k)