class Solution:
    def numberOfWays(self, cor: str) -> int:
        c = Counter(cor)
        res = 1
        MOD = 10 ** 9 + 7
        #print(c)
        if c["S"] == 2:
            return 1
        elif c["S"] % 2 or c["S"] == 0:
            return 0
        
        count = 1
        couch = 0
        for i in range(len(cor)):
            if cor[i] == 'S':
                if couch == 2:
                    res *= count
                    res %= MOD
                    count = 1
                    couch = 0
                couch += 1
            elif cor[i] == 'P':
                if couch == 2:
                    count += 1
            
                
            
        return res % MOD