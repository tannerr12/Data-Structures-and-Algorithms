class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        idx1 = 0
        idx2 = 0
        p1 = 0
        p2 = 0
        
        res = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            
            if nums1[idx1] == nums2[idx2]:
                res += (max(p1,p2) + nums1[idx1]) % MOD
                res %= MOD
                idx1 += 1
                idx2 += 1
                p1,p2 = 0,0
                
                
            elif nums1[idx1] < nums2[idx2]:
                p1 += nums1[idx1]
                idx1 += 1
            else:
                p2 += nums2[idx2]
                idx2 += 1
        
        
        while idx1 < len(nums1):
            p1 += nums1[idx1]
            idx1 += 1
        while idx2 < len(nums2):
            p2 += nums2[idx2]
            idx2 += 1
        

            
        res += max(p1,p2) % MOD
       
        return res % MOD
        