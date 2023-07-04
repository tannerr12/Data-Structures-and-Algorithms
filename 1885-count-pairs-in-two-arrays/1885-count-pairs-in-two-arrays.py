class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:

        
        diff = []
        for i in range(len(nums1)):
            diff.append(nums1[i] - nums2[i])
        
        
        diff.sort()
        res = 0
        #print(diff)
        for i in range(len(diff)):
            
            #1 -> 0
            #0 -> 1
            #-1 -> 2
            #-2 -> 3
            #2 -> -1
            if diff[i] <= 0:
                continue
            find = (diff[i] * -1) 
            
            idx = bisect_right(diff, find)
            
            
            res += i - idx
        
        return res
            
            
            