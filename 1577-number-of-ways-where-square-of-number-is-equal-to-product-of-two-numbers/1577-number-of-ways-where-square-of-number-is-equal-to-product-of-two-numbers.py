class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        
        for val in nums1:
            mp1[val ** 2] += 1
        
        for val in nums2:
            mp2[val ** 2] += 1
        
        
        res = 0
        
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                val = nums1[i] * nums1[j]
                if val in mp2:
                    res += mp2[val]
        
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                val = nums2[i] * nums2[j]
                if val in mp1:
                    res += mp1[val]
        
        return res
                
            