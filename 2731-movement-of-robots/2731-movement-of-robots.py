class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
  
        
        for i in range(len(nums)):
            
            if s[i] == 'L':
                
                nums[i] = nums[i] - d
                
            else:
                nums[i] = nums[i] + d
                
        
        
        nums.sort()
        
        MOD = 10 ** 9 + 7
        res = 0
        left = 0
        for i in range(len(nums)):
            
            res += nums[i] * i - left
            left += nums[i]
            res %= MOD
            left %= MOD
            
        
        return res
        