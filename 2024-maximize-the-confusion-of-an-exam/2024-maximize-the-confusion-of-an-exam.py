class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        
        
        T = 0
        F = 0
        l = 0
        cur = 0
        res = 0
        
        for i in range(len(answerKey)):
            
            char = answerKey[i]
            if char == "T":
                T +=1
            else:
                F +=1
                
            
            while i - l + 1 > T + k and i - l + 1 > F + k:
                
                char = answerKey[l]
    
                if char == "T":
                    T -=1
                else:
                    F -=1
                
                l+=1
            
            
            if T + k >= k or F + k >= k:
                res = max(res, i - l +1)
    
        
        
        return res