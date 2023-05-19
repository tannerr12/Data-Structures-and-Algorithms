class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        
        if s1 == s2:
            return 0

        res = 0
        if s1 > s2:
            nums1,nums2 = nums2,nums1
            s1,s2 = s2,s1
        
        if len(nums1) * 6 < len(nums2):
            return -1
        
        gap = s2 - s1
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        for i in range(1,6):
            take = math.ceil(gap / (6 - i))
            mx = (c1[i] * (6 - i)) + (c2[7-i] * (6 - i))
                
            if mx < take * (6-i):
                res += c1[i] + c2[7-i]
                gap -= mx
            else:
                res += take
                gap = 0
            if gap <= 0:
                break
    
        return res
            
            
            
        
        
        