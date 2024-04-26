class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        #remove = [False] * len(strs[0])
        strs.sort()
        
        @cache
        def isGood(i, target, last):
            
            if i >= len(strs[0]):
                return True
            
            res = False
            canTake = True
            if last != -1:
                
                for j in range(len(strs)):
                    if strs[j][last] > strs[j][i]:
                        canTake = False
                        break
                
                if target > 0:
                    res = res or isGood(i+1, target -1, last)
                    
            else:
                if target > 0:
                    res = res or isGood(i+1, target -1, last)
            
            if canTake:
                res = res or isGood(i+1, target, i)
                
            return res
            
            
        l,r = 0, len(strs[0])
        
        while l < r:
            
            mid = (l+r) // 2
            
            if isGood(0, mid, -1):
                r = mid 
            else:
                l = mid + 1
        
        
        return l
                