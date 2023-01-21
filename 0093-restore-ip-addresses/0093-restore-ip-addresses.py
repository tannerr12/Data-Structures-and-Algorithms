class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        arr = set()
        memo = {}
        
        def backtrack(i,cur,full,count):
            
            if count > 4:
                return 
            if i >= len(s):
                if count != 4:
                    return
                arr.add(full)
                return 
            
            if full in memo:
                return 
            
            memo[full] = True
            
            
            #add dot 
            if cur != -1:
                
                backtrack(i,-1,full + '.',count + 1)
                
            #dont add
            if cur == -1:
                val = int(s[i])
            else:
                val = int(str(cur) + s[i])
           
            if val <= 255 and cur != 0:
                backtrack(i+1, val,full + s[i],count)
                
            
            
            
        
        
        
        backtrack(0,-1,'',1)
        
        return arr
            