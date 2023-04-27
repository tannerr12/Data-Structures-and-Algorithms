class Solution:
    def countHomogenous(self, s: str) -> int:
        
        #count = Counter(s)
        res = 0
        MOD = 10 ** 9 + 7
        
        curChar = ''
        size = 0
        
        mp = defaultdict(int)
        for i, e in enumerate(s):
            
            if e == curChar:
                size +=1
            else:
                if size > 0:
                    mp[curChar * size] += 1
                curChar = e
                size = 1
        
        mp[curChar * size] += 1
        
        res = 0
        
        for key,val in mp.items():
            res += ((len(key) * (len(key) + 1)) // 2) * val
            res %= MOD
        
        
        return res % MOD
        #print(mp)
            
            
        