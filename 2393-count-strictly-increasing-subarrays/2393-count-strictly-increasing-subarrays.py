class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        dp = [0] * len(nums)
        dp[1] = 1
        
        for i in range(2,len(nums)):
            dp[i] = dp[i-1] + i
        
        
        print(dp)
        """
        consec = 0
        res = 0
        for i in range(len(nums)):
        
            if i == 0:
                consec +=1
                res += consec
            
            else:
                
                if nums[i-1] < nums[i]:
                    consec+=1
                
                else:
                    consec = 1
                
                
                res += consec
        
        return res
                
            
            
            
            