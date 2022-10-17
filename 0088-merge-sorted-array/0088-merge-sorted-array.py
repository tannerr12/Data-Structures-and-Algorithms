class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x,y = 0,0
        res = []
        while True:
            if x >= m and y >= n:
                break
            
            if (y >= n and x < m) or (x < m and nums1[x] <= nums2[y]):
                res.append(nums1[x])
                x+=1
            else:
                res.append(nums2[y])
                y+=1
        
        for i in range(len(res)):
            nums1[i] = res[i]
            
                
            