class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        #get our counter of our input
        count = Counter(str(n))
        
        #now we just compare the count of digits to any of the powers of 2
        #go through 30 bit positions
        for i in range(31):
            num = 0 | (1 << i)
            nCount = Counter(str(num))
            if count == nCount:
                return True
        
        return False
        
        
        """
        mask = 0
        
        n = str(n)
        N = len(n)
        for i in range(N):
            mask |= (1 << i)
        @cache
        def backtrack(bitmask,num):
            
            if bitmask ^ mask == 0:
                
                if num & (num-1) == 0:
                    return True
                return False
            
            res = False
            for i in range(N):
                
                if (num == 0 and n[i] == '0') or bitmask & (1 << i) != 0:
                    continue
                
                res = res or backtrack(bitmask | (1<< i), (num * 10) + int(n[i]))
            
            
            return res
        
        return backtrack(0,0)
        
        """