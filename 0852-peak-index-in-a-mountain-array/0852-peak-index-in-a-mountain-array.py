class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        l,r = 0, len(arr) -1
        if len(arr) < 3:
            return 0
        
        while l <= r:
            
            curr = (l+r) // 2
            
            
            if curr != len(arr) -1 and curr != 0 and arr[curr] > arr[curr +1] and arr[curr] > arr[curr -1]:
                return curr
            
            elif arr[curr] > arr[curr -1] or curr == 0:
                l = curr +1
            else:
                r = curr -1
                
        
        
        return l
                
            