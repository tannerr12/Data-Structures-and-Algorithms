class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def isGood(val):

            target = val * n
            s = 0
            for i in range(len(batteries)):
                
                s+= min(batteries[i], val)
            
            
            return s >= target
            
            
                
        
        
        
        l,r = 0, 10**15
        res = 0
        while l <= r:
            
            mid= (l+r)//2
            
            if isGood(mid):
                res = mid
                l = mid +1
            else:
                r = mid -1
                
        return res
        