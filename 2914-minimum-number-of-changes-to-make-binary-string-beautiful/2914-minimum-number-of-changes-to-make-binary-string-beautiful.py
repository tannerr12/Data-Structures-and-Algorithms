class Solution:
    def minChanges(self, s: str) -> int:
        one = 0
        zero = 0
        score= 0
        for i in range(len(s)):
            char = s[i]
            
            if char == "0":
                zero += 1
            
            else:
                one +=1
                
            
            if i % 2 == 1 and zero == one:
                score += 1
                one = 0
                zero = 0
            elif i % 2 == 1:
                one = 0
                zero = 0
        
        return score
                
            