class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        calc = {}
        res = 0
        score = 0
        for i in range(len(hours)):
            
            if hours[i] > 8:
                score +=1
            else:
                score -=1
            
            if score not in calc:
                calc[score] = i  
            
            if score > 0:
                res = max(res, i + 1)
            elif score - 1 in calc:
                res = max(res, i - calc[score-1] )
        
        
        return res
   