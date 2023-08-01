class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        col = len(encodedText) // rows
        
        words = defaultdict(list)
        res = ''
        for j in range(col):
            nonspace = False
            for i in range(j,len(encodedText), col + 1):
                words[j].append(encodedText[i])
                if encodedText[i] != ' ':
                    nonspace = True
            #if nonspace:     
            res += ''.join(words[j])
        #print(words[0])
        #print(words[1])
        
        
        idx = len(res) -1 
        while idx >= 0 and res[idx] == ' ':
            idx -=1
        
        
        return res[:idx+1]
            
            