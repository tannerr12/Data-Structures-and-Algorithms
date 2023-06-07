class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i):

            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            # calculate the number per group of 2
            res =0

            if s[i] != '*':
                #jump 1 is always possible
                res += dfs(i+1) 
            else:
                res += dfs(i+1) * 9
            
            if i < len(s) -1 and s[i] == '*' and s[i+1] == '*':
                res += dfs(i+2) * 15
            elif i < len(s) -1 and s[i] == '*':
                nxt = int(s[i+1])
                if nxt <= 6:
                    res += dfs(i+2) * 2
                else:
                    res += dfs(i+2)
            elif i < len(s) -1 and s[i+1] != '*' and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i + 1]) <= 6)):
                res += dfs(i+2)
            elif i < len(s) -1 and s[i+1] == '*' and (int(s[i]) == 1 or int(s[i]) == 2):
                mx = 10
                if int(s[i]) == 1:
                    mx = 9
                else:
                    mx = 6
                
                res += dfs(i+2) * mx
                 
            
            return res % MOD
              
        
        return dfs(0) % MOD