class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        lmax = nums[0]
        
        local = nums[0]
        size =1 
        res = 1
        for i in range(1,len(nums)):
            
            local &= nums[i]
           
            
            if local >= lmax and local >= nums[i]:
                size +=1
                res = max(res,size)

            else:
                if nums[i] > lmax:
                    res = 1
                else:
                    res = max(res,size)
                local = nums[i]
                size = 1
                #res = max(res,size)
            lmax = max(local,lmax,nums[i])
        
        return res
            
            
            
            