class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        c = defaultdict(int)
        
        
        for val in arr:
            
            c[val % k] += 1
        
        
        for key in list(c):
            if key not in c or c[key] == 0:
                continue
            mod = key
            opp = k - mod

            if mod == 0:
                if c[mod] % 2:
                    return False
                else:
                    c[mod] = 0
                    del c[mod]
                    continue

            if opp in c:
                
                c[opp] -= c[mod]
                c[mod] = 0
                if c[opp] < 0:
                    return False
                
                if c[opp] == 0:
                    del c[opp]
                if c[mod] == 0:
                    del c[mod]
            else:
                return False

        
        return len(c) == 0
            
        