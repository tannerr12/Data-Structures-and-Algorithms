class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        idx = [len(nums)] * len(nums)
        prev = len(nums)
        for i in range(len(nums) -1,-1,-1):
            
            if nums[i] == 1:
                idx[i] = prev
                prev = i
            else:
                idx[i] = prev
        
        
        #print(idx)
        
        
        
        
        l = 0
        s = 0
        res = 0
        for i in range(len(nums)):
            
            s += nums[i]
            
            while l < len(nums) and l <= i and s >= goal:
                if s == goal:
                    res += 1 + (idx[i] - (i + 1))
                s-=nums[l]
                l +=1
                
            
        return res    
        
        