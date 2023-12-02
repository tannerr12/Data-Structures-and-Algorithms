class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res = 1
        
        l = 0
        
        for r in range(1, len(arr)):
            
            mod = r % 2
            
            if mod and arr[r-1] >= arr[r]:
                l = r
            
            elif mod == 0 and arr[r-1] <= arr[r]:
                l = r
                
            
            res = max(r-l + 1,res)
        
        
        l = 0
        for r in range(1, len(arr)):
            
            mod = r % 2
            
            if mod == 0 and arr[r-1] >= arr[r]:
                l = r
            
            elif mod and arr[r-1] <= arr[r]:
                l = r
                
            
            res = max(r-l + 1,res)
            
        
        return res