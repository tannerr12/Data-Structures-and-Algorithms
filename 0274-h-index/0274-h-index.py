class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        def isGood(mid):
            
            count = 0
            
            for val in citations:
                
                if val >= mid:
                    count +=1
                
                
            return count >= mid
            
        
        l,r = 0, 1000
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                l = mid +1
                
            else:
                r = mid -1
                
        
        
        return res