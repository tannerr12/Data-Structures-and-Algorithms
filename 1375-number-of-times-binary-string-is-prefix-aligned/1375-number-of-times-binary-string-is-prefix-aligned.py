class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        
        
        res = 0
        cur = 0
        for i in range(len(flips)):
            cur = max(cur,flips[i])
            if i + 1 == cur:
                res += 1
        return res
                
            
        
        '''
        bit = [0] * (len(flips) + 1)
        def update(x):
            while x < len(bit):
                bit[x] += 1
                x += x & -x

        def find(x):
            total = 0
            while x > 0:    
                total += bit[x]
                x -= x & -x

            return total
        
        
        res = 0
        for i in range(len(flips)):
            update(flips[i])
            res += (find(i + 1) == (i + 1))
        
        return res
        
        '''
            