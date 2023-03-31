class Solution:
    def maximumRemovals(self, s: str, p: str, rem: List[int]) -> int:
        
        def isGood(mid):
            se = set(rem[:mid])
            j = 0
            for i in range(len(s)):
                if i in se:
                    continue
                
                if s[i] == p[j]:
                    j+=1
                    if j == len(p):
                        return True
            
            return False
                    
                
                
        
        
        
        l,r = 0, len(rem) 
        
        res = 0
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                
                res = mid
                l = mid + 1
                
            else:
                r = mid -1
                
        
        
        return res