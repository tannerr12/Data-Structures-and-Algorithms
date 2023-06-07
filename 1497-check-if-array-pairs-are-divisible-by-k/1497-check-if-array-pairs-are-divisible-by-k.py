class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        c = defaultdict(int)
        
        
        for val in arr:
            
            c[val % k] += 1
        
        
        for key in list(c):
            
            while key in c and c[key] > 0:
                mod = key
                opp = k - mod
                
                if mod == 0:
                    opp = 0

                if opp in c:
                    c[opp] -=1
                    c[mod] -=1
                    if c[opp] == 0:
                        del c[opp]
                    if c[mod] == 0:
                        del c[mod]
                else:
                    return False
            
        
        return len(c) == 0
            
        