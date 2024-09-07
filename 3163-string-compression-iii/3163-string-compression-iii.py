class Solution:
    def compressedString(self, word: str) -> str:
        arr = []
        char = ''
        count = 0
        
        for i in range(len(word)):
            c = word[i]
            if i == 0:
                char = c
                count = 1
            else:
                
                if c == char:
                    
                    if count == 9:
                        arr.append(str(count) + str(char))
                        count = 0
                        
                    count += 1
                    
                else:
                    
                    arr.append(str(count) + str(char))
                    
                    count = 1
                    char = c
        
        
        arr.append(str(count) + str(char))          
        
        
        return ''.join(arr)