class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        #1,317 13,1,7
        MOD = 10 ** 9 + 7

        
        @cache
        def dfs(i):
            
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            
            res = 0
            idx = i
            current = 0
            while idx < len(s) and current < k:
                current *= 10
                current += int(s[idx])
              
                
                if current <= k:
                    res += dfs(idx + 1) % MOD
                else:
                    break
                
                idx +=1
        
            
            
            return res % MOD
        
        
        
        return dfs(0) % MOD