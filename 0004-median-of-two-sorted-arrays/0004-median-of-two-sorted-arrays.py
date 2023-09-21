class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A,B = nums1, nums2
        
        size = len(A) + len(B)
        half = size //2
        if len(B) < len(A):
            A,B = B,A
        
        
        
        #find where nums2[0] >= nums1 and nums1 [+1] >= nums2[0] merge here 
        # or nums 2[end] <= nums1[0]
        #check which is larger start left or start right
        
        
        def binarySearch():
            
            l = 0
            
            r = len(A) -1
            
            while True:
                i = (l+r) // 2
                j = half - i - 2
                
                
                
                leftA = A[i] if i >= 0 else float('-inf')
                leftB = B[j] if j >= 0 else float('-inf')
                rightA = A[i+1] if i < (len(A)-1) else float('inf')
                rightB = B[j+1] if j < (len(B)-1) else float('inf')
                
                
                if rightA >= leftB and rightB >= leftA:
                    
                    if size % 2:
                        return min(rightA,rightB)
                    
                    return (max(leftA, leftB) + min(rightA,rightB)) / 2
                
                elif rightB < leftA:
                    r = i -1
                
                else:
                    l = i +1
                

            
        
        
        return binarySearch()