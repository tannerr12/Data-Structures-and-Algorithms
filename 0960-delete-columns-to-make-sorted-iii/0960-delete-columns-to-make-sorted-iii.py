class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        #remove = [False] * len(strs[0])

        
        @cache
        def isGood(i, last):
            
            if i >= len(strs[0]):
                return 0
            
            res = len(strs[0])
            canTake = True
            if last != -1:
                
                for j in range(len(strs)):
                    if strs[j][last] > strs[j][i]:
                        canTake = False
                        break
                
                
                res = min(res, isGood(i+1, last) + 1)
                    
            else:
                res = min(res, isGood(i+1, last) + 1)
            
            if canTake:
                res = min(res, isGood(i+1, i))
                
            return res
            
        
        return isGood(0, -1)
