class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        

        res = float('inf')
        def good(target):
            
            m1 = target // divisor1
            m2 = target // divisor2
            
            both = target // math.lcm(divisor1, divisor2)
            
            
            return target - both >= uniqueCnt1 + uniqueCnt2 and target - m1 >= uniqueCnt1 and target - m2 >= uniqueCnt2
        
        
        #res = max(max(res1), max(res2))
        
        
        #binary search over boundaries
        
        l,r = 0 , 1 << 32 -1
        
        while l<=r:
            
            curr = (l+r)//2
            
            if good(curr):
                r = curr - 1
                res = min(res,curr)
            else:
                l = curr + 1
        
        
        
        
        
        return res