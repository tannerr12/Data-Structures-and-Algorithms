class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        count = Counter(text)
        
        
        character = {}
        
        l = 0 
        res = 0
        for i in range(len(text)):
            
            if text[i] in character:
                
                character[text[i]] +=1
            
            else:
                character[text[i]] =1
                
            mx = 0
            mxchar = 0
            for key,val in character.items():
                if val > mx:
                    mx = val
                    mxchar = key
                    
            while  (i - l + 1) - mx > 1 or (count[mxchar] - character[mxchar] == 0 and len(character) > 1 and min(character.values()) != mx):
                
                character[text[l]] -=1
                if character[text[l]] == 0:
                    del character[text[l]]
                
                l +=1
                mx = 0
                for key,val in character.items():
                    if val > mx:
                        mx = val
                        mxchar = key
         
            
            for char,val in character.items():
             
                if count[char] - val >= 1 and i - l + 1 - val == 1:
                    res = max(res, i - l + 1)
                elif i - l + 1 - val == 0:
                    res = max(res,i-l+1)
            
            
        
        
        return res