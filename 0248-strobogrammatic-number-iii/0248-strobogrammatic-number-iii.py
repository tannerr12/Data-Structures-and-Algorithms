class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        #strobogrammic
        #1, 0, 8
        #100, 88,81
        
        res = 0

        @cache
        def dfs(cur,d):
            a = 0
            c1,c2 = '',''
            if d == 0:
                
               
                nex = ''
                for i in range(len(cur)-2,-1,-1):
                    if cur[i] == '6':
                        nex += '9'
                    elif cur[i] == '9':
                        nex += '6'
                    else:
                        nex += cur[i]
                c1 = cur + nex


                nex = ''
                for i in range(len(cur)-1,-1,-1):
                    if cur[i] == '6':
                        nex += '9'
                    elif cur[i] == '9':
                        nex += '6'
                    else:
                        nex += cur[i]
                c2 = cur + nex
                    
            if d == 0 and ((len(c1) == len(low) and low <= c1) or len(c1) > len(low)) and (len(high) > len(c1) or (len(high) == len(c1) and c1 <= high)) and not (len(c1) % 2 and c1[len(c1)//2] in ['6', '9']) and len(c1) > 1:
                a = 1
            if d == 0 and ((len(c2) == len(low) and low <= c2) or len(c2) > len(low)) and (len(high) > len(c2) or (len(high) == len(c2) and c2 <= high)):
                a += 1
            if d == 0:
                return a
            
            res = 0    
            
            for val in ['0', '1', '8', '6', '9']:
                if len(cur) == 0 and val == '0':
                    continue
                
                res += dfs(cur + val,d-1)
            
            return res 
        
        ans = 0
        if len(low) == 1:
            for i in range(0, 10):
                if str(i) >= low and str(i) in ['0', '1', '8']:
                    if len(high) == 1 and str(i) > high:
                        continue
                    ans += 1
             
        for i in range(1, len(high) // 2 + 2):
            ans += dfs('', i)
        
        return ans