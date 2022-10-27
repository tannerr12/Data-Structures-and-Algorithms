class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        res = 0
        
        
        
        for i in range(len(nums1)):
            
            n = nums1[i]
            
            
            l,r = i , len(nums2) -1
            
            
            while l <= r:
                
                curr =  (l+r)// 2
                
                
                if nums2[curr] >= nums1[i]:
                    res = max(res,curr - i)
                    l = curr +1
                
                
                elif nums2[curr] < nums1[i]:
                    r = curr -1
                    
        
        
        return res