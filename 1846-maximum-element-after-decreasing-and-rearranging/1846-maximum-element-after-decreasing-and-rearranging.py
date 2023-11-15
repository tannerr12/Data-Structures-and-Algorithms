class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        last = arr[0]
        
        
        for i in range(1,len(arr)):
            
            if arr[i] - last > 1:
                last = last + 1
            
            else:
                last = arr[i]
                
        
        return last