class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero = 0
        res = 0
        for i in range(len(nums)):
            
            if nums[i] == 0:
                zero+=1
            
            else:
                res += (zero * (zero + 1)) // 2
                zero = 0
        
        return res + (zero * (zero + 1)) // 2
            