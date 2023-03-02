class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        count = 0
        for i in range(len(words[0])):
            w = ''
            for j in range(len(words)):
                if i >= len(words[j]):
                    continue
                w += words[j][i]
                
            
         
            if w != words[count]:
                return False
            
            count +=1
        
        return True
                