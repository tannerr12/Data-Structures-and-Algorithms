class Solution:
    def numSteps(self, s: str) -> int:
        
        
        arr = list(s)
        l = len(arr)-1
        r = len(arr)-1
        res = 0
        while l > 0:
            
            while l > 0 and arr[l] == '0':
                l -=1
                res +=1
            
            if l == 0:
                return res
            
            if r >= l -1:
                r = l -1
            while r > 0 and arr[r] != "0":
                r -=1
            
            if r == 0 and arr[r] == '1':
                res += l + 2
                break
                
            arr[r] = '1'
            l-=1
            res +=2
            
        
        return res
                
        
            