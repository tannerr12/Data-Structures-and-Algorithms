class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        for i in range(len(nums2)):
            nums2[i] = [nums2[i], i]
            
        
        
        nums1.sort()
        nums2.sort()
        
        res = [0] * len(nums1)
        
        l,r = 0,len(nums1)-1
        idx = len(nums2)-1
        while l <= r:
            
            while l <= r and nums1[r] <= nums2[idx][0]:
                
                res[nums2[idx][1]] = nums1[l]
                l+=1
                idx -=1
            
            if r >= l and nums1[r] > nums2[idx][0]:
                res[nums2[idx][1]] = nums1[r]
                r -=1
                idx -=1
        
        
        return res
                