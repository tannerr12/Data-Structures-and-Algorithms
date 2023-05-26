class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        res = 0
        mn,mx = 0,0
        sub = 0
        
        for i in range(len(target)):
            v = target[i] - sub
            if v < 0:
                #below 0 pay the cost by incrementing it by its abs(val)
                res += (v * -1) 
                #we can no longer use the extra negative values in our across the board subtraction so we need to remove them
                sub -= (v * -1)
                
            
            if v > mn:
                sub += mn
                res += mx - mn
                mx,mn = 0, float('inf')
                
            
            
            mn = min(mn, target[i]-sub)
            mx = max(mx, target[i]-sub)
        
        

        return res + sub + mx