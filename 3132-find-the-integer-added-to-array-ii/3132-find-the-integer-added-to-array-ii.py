class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1.sort()
        nums2.sort()
        res = float('inf')
        
        def check(i,j):
            diff = 0
            dist = float('inf')
            for k in range(len(nums1)):
                if k == i or k == j:
                    diff +=1
                    continue
                if dist == float('inf'):
                    dist = nums2[k-diff] - nums1[k]
                elif nums2[k-diff] - nums1[k] != dist:
                    return float('inf')
            
            return dist
        
        for i in range(n):
            for j in range(i+1, n):
                res = min(res, check(i,j))
        
        
        return res