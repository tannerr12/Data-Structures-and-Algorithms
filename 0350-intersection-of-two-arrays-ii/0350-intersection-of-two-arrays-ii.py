class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = Counter(nums1)
        y = Counter(nums2)
        res = []
        
        for i in range(len(nums1)):
            
            
            if x[nums1[i]] > 0 and nums1[i] in y and y[nums1[i]] > 0:
                
                for j in range(min(x[nums1[i]], y[nums1[i]])):
                    res.append(nums1[i])
                
                
                x[nums1[i]] = 0
                y[nums1[i]] = 0
        
        
        return res