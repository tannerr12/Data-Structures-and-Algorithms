class Solution:
    def minFlips(self, target: str) -> int:
        flipped = False
        res = 0
        for i in range(len(target)):
            
            if target[i] == '1' and flipped == False:
                flipped = True
                res +=1
            
            
            elif target[i] == '0' and flipped:
                flipped = False
                res +=1
        
        
        return res