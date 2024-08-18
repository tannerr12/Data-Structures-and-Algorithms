class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        both = set(nums1 + nums2)
        need1 = len(nums1)//2
        need2 = len(nums2)//2
        
        need1 -= len(nums1) - len(c1)
        need2 -= len(nums2) - len(c2)
        
        remain = max(0, need1) + max(0, need2)
        
        if remain == 0:
            return len(both)
        
        
        for key in both:
            
            if c1[key] > 0 and c2[key] > 0:
                remain -=1
        
        
        if remain <= 0:
            return len(both)
        else:
            return len(both) - remain
        
            