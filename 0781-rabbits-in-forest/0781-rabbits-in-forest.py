class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        
        c = Counter(answers)
        res = 0
        for key,val in c.items():
            remaining = val % (key + 1)
            if remaining == 0:
                continue
            res += key - remaining +1
                
        
        return res + len(answers)