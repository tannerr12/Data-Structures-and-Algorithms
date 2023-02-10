class Solution:
    def minSwaps(self, s: str) -> int:
        
        arr = list(s)
        res = 0
        
        stack = []
        l,r = 0, len(s) -1
        while l < r:
            
            while r > l and arr[r] == ']':
                r -=1
            
            if l == r:
                break
            if not stack and arr[l] == ']':
                arr[l],arr[r] = arr[r],arr[l]
                res +=1
                stack.append(arr[l])
            
            elif stack and arr[l] == ']':
                stack.pop()
            
            else:
                stack.append(arr[l])
            
            
            l+=1
        
        
    
        
        return res
            
            
        