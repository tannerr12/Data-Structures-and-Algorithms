class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(z,o,turn):
            
            if z == 0 and o == 0:
                return 1
            
            res = 0
            if turn:
                for i in range(1, min(limit, z) + 1):
                    res += dfs(z - i, o, not turn) % MOD
            else:
                for i in range(1, min(limit, o) + 1):
                    res += dfs(z, o - i, not turn) % MOD
            
            return res % MOD
        
        
        return (dfs(zero, one, True) + dfs(zero, one, False)) % MOD