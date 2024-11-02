class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        frontback = sentence[0] == sentence[-1]
        
        words = sentence.split(' ')
        
        for i in range(1,len(words)):
            
            if words[i][0] != words[i-1][-1]:
                return False
            
        
        return frontback
            