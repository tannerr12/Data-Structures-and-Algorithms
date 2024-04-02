class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        prefix = []
        ppow = []
        
        MOD = 10 ** 9 + 7
        P = 31
        
        ppow.append(1)
        prefix.append(0)
        
        for i in range(1, len(word) + 1):
            ppow.append((ppow[i-1] * P) % MOD)
        
        for i in range(1, len(word) + 1):
            prefix.append((prefix[i-1] + ppow[i] * (ord(word[i-1]) - ord('a') + 1)) % MOD) 
    
    
        
        #print(prefix)
        #print(ppow)
        n = len(word)
        ans = math.ceil(len(word) / k)
        for i in range(n - 1, 0, -1):
            if i % k == 0:
                
                hf = (prefix[n - i] * ppow[i]) % MOD
                hb = (prefix[n] - prefix[i] + MOD) % MOD
                
                if hf == hb:
                    ans = min(ans, math.ceil(i / k))
            
        
        return ans
        
            