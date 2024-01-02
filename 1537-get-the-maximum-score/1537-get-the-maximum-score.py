class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mp = defaultdict(int)
        
        idx1 = 0
        idx2 = 0
        p1 = 0
        p2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            
            if nums1[idx1] == nums2[idx2]:
                mp[nums1[idx1]] = max(p1,p2)
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
        
        end = [p1, p2]
        res = 0
        for key in sorted(mp):
            v1 = mp[key]
            res += v1 % MOD
            res += key % MOD
            res %= MOD
            
        res += max(end[0], end[1])
       
        return res % MOD
        