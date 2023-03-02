class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 1
        count = 1
        prev = chars[0]
        j = 1
        while i < len(chars):
            
            if chars[i] != prev:
                if count > 1:
                    c = str(count)
                    
                    for ch in c:
                        chars[j] = ch    
                        j+=1
                    chars[j] = chars[i]
                    j +=1
                
                else:
                    chars[j] = chars[i]
                    j+=1
                count = 1
                prev = chars[i]
                
            
            else:
                count +=1
                
            
            i +=1
        
        
        if count > 1:
            c = str(count)

            for ch in c:
                chars[j] = ch    
                j+=1
            

        while len(chars) != j:
            chars.pop()
            