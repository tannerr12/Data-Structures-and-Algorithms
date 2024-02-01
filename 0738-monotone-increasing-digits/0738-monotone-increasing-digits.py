class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        if n < 10:
            return n
        
        '''
        def dfs(val,size):
            res = 0
            if val > n:
                return 0
            else:
                res = val 
            
            last = val % 10
            
            for i in range(9,last):
                if i == 0 and val == 0:
                    continue
                    
                newval = val * 10 + i
                
                res = max(res, dfs(newval))
            
            return res
        '''
        #same size
        sn = str(n)
        res = int('9' * (len(sn) -1))
        stack = []
        seq = True
        mx = 0
        for i in range(len(sn)):
            cur = int(sn[i])
            if cur - mx >= 1:
                res = max(res, int(sn[:i] + str(cur - 1) + ('9' * (len(sn) - i - 1))))
            
            if mx > cur:
                seq = False
                break
                
            mx = max(mx,cur)
            
        if seq:
            return n
        
        return res
            
            