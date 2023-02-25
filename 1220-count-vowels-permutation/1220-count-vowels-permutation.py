class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #simple path finding dfs 
        #5*N time complexity, I initially thought it had to be a math solution due to the size of N but 
        #realized after that since vowels is size 5 it passes
        @cache
        def dfs(i,char):
            
            res = 1
            if i > 1:
                
                if char == 'a':
                    res = dfs(i-1, 'e') + dfs(i-1, 'i') + dfs(i-1, 'u')
                
                elif char == 'e':
                    res = dfs(i-1, 'a') + dfs(i-1, 'i')
                
                elif char == 'i':
                    res = dfs(i-1, 'e') + dfs(i-1 , 'o')
                
                elif char == 'o':
                    res = dfs(i-1, 'i')
                
                else:
                    res = dfs(i-1, 'i') + dfs(i-1, 'o')
            
            
            
            return res
        
        
        res = 0
        v = ['a','e','i','o','u']
        
        MOD = 10**9 + 7
        for char in v:
            res += dfs(n, char) % MOD
        
        return res % MOD