class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #length - index == value
        
        
        l, r = 1, len(citations)
        res = 0
        
        while l <= r:
            
            mid = (l+r)//2
            
            val = citations[-(mid)]
            
            
            if val >= mid:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        
        return res 
        