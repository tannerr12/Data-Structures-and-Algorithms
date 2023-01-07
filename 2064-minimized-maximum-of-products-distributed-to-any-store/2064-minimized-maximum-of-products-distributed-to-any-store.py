class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        
        def isGood(val):
            if val == 0:
                return False
            i = 0
            local = val
            store = 0
            while i < len(quantities):
                v = quantities[i]
                
                
                store += math.ceil(v / val)
                
                if store > n:
                    return False
                
                
                i +=1
            
            return store <= n
                        
                
                
                
        
        
        l,r = (sum(quantities) // n) , sum(quantities)
        
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                r = mid -1
                
            else:
                l= mid +1
        
        return res