class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        h = set(sentence)
        
        return len(h) == 26
        
       
        
        for i in range(26):
            
            if chr(ord('a') + i) not in h:
                return False
        
        
        return True
        