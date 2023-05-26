class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        res = 0
        mx = target[0]
        sub = 0
        
        for i in range(1,len(target)):
        
            if target[i] - sub < 0:
                #below 0 pay the cost by incrementing it by its abs(val)
                res += ((target[i] - sub) * -1) 
                #we can no longer use the extra negative values in our across the board subtraction so we need to remove them
                sub -= ((target[i] - sub) * -1)

            if target[i] - sub > target[i-1]-sub:
                res += mx - (target[i-1]-sub)
                sub += target[i-1]-sub
                mx = target[i]-sub

        return res + sub + mx