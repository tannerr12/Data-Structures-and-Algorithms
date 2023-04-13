class Solution:
    def numSteps(self, s: str) -> int:
        
        
        arr = list(s)
        
        r = len(arr)-1
        res = 0
        while len(arr) > 1:
            
            while len(arr) > 1 and arr[-1] == '0':
                arr.pop()
                res +=1
            
            if len(arr) == 1:
                return res
            
            while r > len(arr)-1 or (r > 0 and arr[r] != "0"):
                r -=1
            
            if r == 0 and arr[r] == '1':
                res += len(arr) + 1
                break
                
            arr[r] = '1'
            arr[-1] = '0'
            res +=1
            
        
        return res
                
        
            