class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
 #       h = collections.defaultdict(int)
  #      for i in range(len(nums1)):
   #         h[nums1[i]] = i
            
        
    #    curr = -1
        res = []
        for j in range(len(nums1)):
            start = False
            found = False
            for i in range(len(nums2)):
                if nums2[i] > nums1[j] and start:
                    res.append(nums2[i])
                    found = True
                    break
                if nums1[j] == nums2[i]:
                    start = True
                    #nums1[h[nums2[i]]] = curr

                #curr = max(curr,nums2[i])
            if not found:
                res.append(-1)
        
        print(res)
        
        
        return res