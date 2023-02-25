class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        pairs = defaultdict(int)
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                val = nums3[i] + nums4[j]
                pairs[val] +=1
        
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                target = (nums1[i] + nums2[j]) * -1
                if target in pairs:
                    res += pairs[target]
        
        return res
                
            