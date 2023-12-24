class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1,s2 = 0,0
        z1,z2 = 0,0
        
        
        for num in nums1:
            if num == 0:
                z1 += 1
            
            s1 += num
        
        for num in nums2:
            if num == 0:
                z2 += 1
            
            s2 += num
            
        if z1 == 0 and s1 < (s2 + z2):
            return -1
        if z2 == 0 and s2 < (s1 + z1):
            return -1
        return max(s1 + z1, s2 + z2)
            
            
            
            
            
        
        