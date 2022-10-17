class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        h = Counter(sentence)
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(alpha)):
            
            if alpha[i] not in h:
                return False
        
        
        return True
        