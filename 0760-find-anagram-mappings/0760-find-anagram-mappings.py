class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        
        for i,val in enumerate(nums2):
            
            mp[val] = i
        
        res = [0] * len(nums1)
        
        for i,val in enumerate(nums1):
            
            res[i] = mp[val]
            
        
        return res
        
        