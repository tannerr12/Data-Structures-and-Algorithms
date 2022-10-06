class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        dp = []
        res = 2
        for i in range(1,len(nums)):
            
            val = nums[i-1] - nums[i]
            
            if val != 0:
                dp.append(val)
                
        
        if len(dp)== 0:
            return 1
        
        for i in range(1,len(dp)):
            
            if (dp[i-1] < 0 and dp[i] > 0) or (dp[i-1] >0 and dp[i] < 0):
                res+=1
                
        
        
        return res
            