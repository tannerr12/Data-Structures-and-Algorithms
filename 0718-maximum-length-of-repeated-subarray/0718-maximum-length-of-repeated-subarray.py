class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        res1 = set()
        #res2 = set()
        
        for i in range(len(nums1)):
            s = str(nums1[i])
            res1.add(s)
            for j in range(i + 1,len(nums1)):
                s += ',' + str(nums1[j])
                res1.add(s)
        
        res = 0
        for i in range(len(nums2)):
            s = str(nums2[i])
            if s in res1:
                res = max(res,1)
                for j in range(i + 1,len(nums2)):
                    s += ',' + str(nums2[j])
                    if s in res1:
                        res = max(res,j - i + 1)
                    else:
                        break
        
        
        return res
                
        
        