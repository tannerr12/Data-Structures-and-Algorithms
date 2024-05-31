class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 
        
        for n in nums:
            xor ^= n
            
        firstbit = xor & (xor-1) ^ xor
        num1 = 0
        for n in nums:
            if n & firstbit:
                num1 ^= n
            
            
        return [num1,num1^xor]