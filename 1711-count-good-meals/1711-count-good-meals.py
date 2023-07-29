class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        c = Counter(deliciousness)
        res = 0
        for key in c:
            
            for j in range(22):
                v2 = 2 ** j
                
                if v2 >= key:
                    if v2-key != key:
                        res += c[key] * c[v2 - key]
                    else:
                        res += (c[key] * (c[key] -1)) // 2
                    res %= MOD
            c[key] = 0
        return res 
                    
        #1234
        #12
        #13
        #14
        #23
        #24
        #34