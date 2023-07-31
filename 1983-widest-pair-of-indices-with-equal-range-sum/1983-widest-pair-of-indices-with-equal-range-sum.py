class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        
        prefix1 = []
        prefix1.append(0)
        prefix2 = []
        prefix2.append(0)
        
        mp = defaultdict(int)
        count1 = 0
        count2 = 0
        
        res = 0
        
        #0,1,2,2,3
        #0,0,1,2,2
        count1 = 0
        count2 = 0
        for i in range(len(nums1)):
            if count1 - count2 not in mp:
                mp[count1 - count2] = i
            
            count1 += nums1[i]
            count2 += nums2[i]
            
            if count1 - count2 in mp:
                res = max(res, i - mp[count1-count2] + 1)
        
        
        return res
            #prefix1.append(nums1[i] + prefix1[-1])
            #prefix2.append(nums2[i] + prefix2[-1])
        
        
        #print(prefix1)
        #print(prefix2)
        
        