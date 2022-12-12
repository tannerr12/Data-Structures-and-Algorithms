class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        h1 = Counter(nums1)
        h2 = Counter(nums2)
        
        x, y = min(h1.keys()), max(h2.keys())
        r = 0
        
        size = len(nums1)
        while True:
            
            r += x * y
            
            h1[x] -=1
            h2[y] -=1
            size -=1
            if size == 0:
                return r
            if h1[x] == 0:
                x+=1
                while x not in h1:
                    x+=1
            if h2[y] == 0:
                y-=1
                while y not in h2:
                    y-=1
        
        
        res = 0
        for i in range(len(nums1)):
            res += nums1[i] * nums2[i]
            
        
        
        return res