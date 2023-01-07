class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        
        def isGood(val):
            i=0
            pile = 0
            local = val
            while i < len(candies):
                cand = candies[i]
                if cand >= local:
                    pile += cand // val 
                    #if cand != 0:
                    #    pile += cand // val
                    #    local %= cand

                
                local = val
                
                i+=1
                if pile > k:
                    break
            
            return pile >= k

        
        l, r = 1, sum(candies)
        
        res = 0
        while l<=r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                l = mid +1
            else:
                r = mid -1
        
        return res