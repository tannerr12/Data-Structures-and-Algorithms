class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        
        count = {}
        
        l = 0
        res = defaultdict(int)
        for i in range(len(s)):
            
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]] = 1
                
            while i - l + 1 > minSize or len(count) > maxLetters:
                
                count[s[l]] -=1
                
                if count[s[l]] == 0:
                    del count[s[l]]
                
                l +=1
                
            
            
            if i - l + 1 >= minSize:
                res[s[l:i+1]] += 1
        
        
        #print(res)
        r = 0
        for key,val in res.items():
            
            r = max(r,val)
        
        
        return r
            
            
        