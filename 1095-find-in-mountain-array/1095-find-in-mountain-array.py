# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, ma: 'MountainArray') -> int:
        
        #find the peak of the mountain 
        #search for target on the left side of the mountain
        #search for target on the right side of the mountain
        
        
        length = ma.length()
        
        #find the peak
        l,r = 0, length - 1
        
        while l < r:
            
            mid = (l+r) // 2
            
            #check current val
            v1 = ma.get(mid)
            #check val to the right
            v2 = float('-inf')
            if mid + 1 < length:
                v2 = ma.get(mid + 1)
            
            if v1 > v2:
                r = mid
            
            else:
                l = mid + 1
            
            
        print(l)    
        
        peak = l
        
        if ma.get(peak) == target:
            return peak
        
        l,r = 0, peak 
        
        while l < r:
            
            mid = (l+r) // 2
            
            v1 = ma.get(mid)
            
            if v1 > target:
                r = mid
            elif v1 < target:
                l = mid + 1
            else:
                return mid
        
        
        l,r = peak + 1, length
        
        while l < r:
            
            mid = (l+r) // 2
            
            v1 = ma.get(mid)
            
            if v1 > target:
                l = mid + 1
            elif v1 < target:
                r = mid
            else:
                return mid
        
        
        return -1