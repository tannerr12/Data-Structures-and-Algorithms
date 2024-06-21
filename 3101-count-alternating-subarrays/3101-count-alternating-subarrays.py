class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        
        res = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                dist = i - l 
                res += (dist * (dist+1)) // 2  
                l = i
        
        
        dist = len(nums) - l
        res += (dist * (dist + 1)) // 2
        
        return res