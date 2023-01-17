class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        
        prefixs = [0]
        
        prefixt = [0]
        
        for i in range(len(s)):
            
            prefixs.append( (ord(s[i]) - ord('a')))
            prefixt.append( (ord(t[i]) - ord('a')))
        
        
        #print(prefixs)
        #print(prefixt)
        
        l = 1
        
        res = 0
        total = 0
        for i in range(1,len(prefixs)):
            
            total += abs(prefixs[i] - prefixt[i])
            
            while total > maxCost:
                
                res = max(res, (i - l))
                total -= abs(prefixs[l] - prefixt[l])
                l+=1
        
        
        
        res = max(res, len(prefixs) - l)
        return res
            