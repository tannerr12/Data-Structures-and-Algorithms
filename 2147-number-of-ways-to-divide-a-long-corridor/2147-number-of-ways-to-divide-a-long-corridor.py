class Solution:
    def numberOfWays(self, cor: str) -> int:
    
        res = 1
        MOD = 10 ** 9 + 7
        
        
        count = 1
        couch = 0
        for i in range(len(cor)):
            if cor[i] == 'S':
                if couch == 2:
                    res = (res * count) % MOD
                    res %= MOD
                    count = 1
                    couch = 0
                couch += 1
            elif cor[i] == 'P':
                if couch == 2:
                    count += 1
            
        
            
        return res % MOD if couch == 2 else 0 