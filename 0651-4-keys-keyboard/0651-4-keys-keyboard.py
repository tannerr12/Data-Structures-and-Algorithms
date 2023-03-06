class Solution:
    def maxA(self, n: int) -> int:
        memo = {}
        if n == 1:
            return 1
        
        #we make the observation that we do not need to create a path for A key presses
        #if it is already in our buffer
        def dfs(count,buffer,size):
            
            if count == n:
                return size
            
            if count > n:
                return float('-inf')
            
            if (count,buffer,size) in memo:
                return memo[(count,buffer,size)]
            res = 0
            
            #select whole screen, copy 
            if count < n-1 and size - buffer > 1:
                res = max(res, dfs(count +3, size, size * 2))
            
            #paste
            res = max(res,dfs(count +1, buffer, size + buffer))
            
            memo[(count,buffer,size)] = res
            
            return res
        
        return dfs(2,1,2)