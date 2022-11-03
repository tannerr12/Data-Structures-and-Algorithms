class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        curMin = float('inf')
        
        curMax = float('-inf')
        
        res = 0
        
        for i in range(len(nums)):
            tnum = nums[i]
            tmin = float('inf')
            for j in range(i , len(nums)):    
        
                tmin = min(tmin,nums[j])
                tnum = max(tnum,nums[j])
                res += abs(tmin - tnum)


        
        return res
            
            