# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        
        def binSearch(l,r,cur,nums):
            best = l
            while l <= r:
                
                mid = (l+r)//2
                
                if nums.at(mid) != cur:
                    r = mid - 1
                else:
                    l = mid + 1
                    best = mid
            
            return best + 1
        
        res = 0
        size = nums.size()
        l = 0
        
        while l < size: 
            val = nums.at(l)
            l = binSearch(l, size-1, val, nums)
            res += 1
        
        
        return res
            