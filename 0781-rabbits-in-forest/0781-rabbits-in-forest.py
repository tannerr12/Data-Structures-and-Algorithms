class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        
        c = Counter(answers)
        

        res = 0
        for key,val in c.items():
            if key == 0:
                continue
        
            remaining = val % (key + 1)
            if remaining == 0:
                continue
            res += key - remaining +1
            #print(remaining)
                
        
        return res + len(answers)