class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        
        res,resCount = 0,0
            
        dp = {}
        
        
        for i in range(len(nums) -1,-1,-1):
            ls, tcount = 1,1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    x,y = dp[j]
                    if  x + 1 > ls:

                        ls = x +1
                        tcount = y
                    elif x + 1 == ls:
                        tcount +=y


            
            dp[i] = [ls,tcount]
            
            
            if ls > res:
                res = ls 
            
                resCount = tcount
            elif res ==ls:
                resCount += tcount
            
            
        
        return resCount
            
            