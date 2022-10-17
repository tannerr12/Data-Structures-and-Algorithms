class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        res = 0
        
        jmin = jmax = jbad = -1
        
        for i in range(len(nums)):
            a = nums[i]
            
            if a > maxK or a < minK:
                jbad = i
            
            if a == minK:
                jmin = i
            if a == maxK:
                jmax = i
            
            res += max(0,min(jmin,jmax) - jbad)
            
        
        
        return res
            
            
            
            