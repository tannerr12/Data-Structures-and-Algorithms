class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        num = 0
        
        for n in nums:
            num ^= n
            
        res = 0
        for i in range(32):
            hasK = False
            hasI = False
            if k & (1 << i) > 0:
                hasK = True
            
            if num & (1 << i) > 0:
                hasI = True
            
            
            if hasK and not hasI:
                res += 1
            elif hasI and not hasK:
                res += 1
        
        return res
            