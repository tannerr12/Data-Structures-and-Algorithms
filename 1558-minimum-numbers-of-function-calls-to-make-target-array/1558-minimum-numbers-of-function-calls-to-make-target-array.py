class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        res = 0
        arr = [0] * len(nums)
        
        mx = 0
        for i,e in enumerate(nums):
            if e == 0:
                continue
            if e % 2:
                res +=1
                e -=1
            m = 0
            while e > 1:
                if e % 2:
                    res +=1
                    e-=1
          
                e //= 2
                m+=1
            
            res += int(e)
            
            if m > mx:
                res += m - mx
                mx = m
        
        
        return res

                
                
            
            