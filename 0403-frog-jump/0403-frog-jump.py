class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        if stones[1] - stones[0] != 1:
            return False
            
        @cache
        def frogJump(i,k,prev,landed):
            
            if i >= len(stones):
                return False
            if i == len(stones) -1 and landed:
                return True
            elif i == len(stones) -1 and not landed:
                return False
            
            
            #4 options we can jump k -1, k, k+1 or skip
            res = False
            if stones[i+1] - prev == k-1:
                res = res or frogJump(i+1,k-1,stones[i+1],True)
            elif stones[i+1] - prev == k:
                res = res or frogJump(i+1,k,stones[i+1],True)
            elif stones[i+1] - prev == k+1:
                res = res or frogJump(i+1,k+1,stones[i+1], True)
            
            if stones[i] > prev + (k + 1):
                return False
            res = res or frogJump(i+1,k,prev,False)
            
            
            return res
        
        
        return frogJump(1,1,stones[1], True)
        
        
            
            
            
            