class Solution:
    def predictPartyVictory(self, s: str) -> str:
        
        r1 = s.count('R')
        d1 = s.count('D')
        banned = set()
        rban = 0
        dban = 0
        while True:

            for i in range(len(s)):
                if i in banned:
                    continue
                if s[i] == 'R' and dban:
                    dban -=1
                    banned.add(i)
                    r1 -=1
                    continue
                elif s[i] == 'D' and rban:
                    rban -=1
                    banned.add(i)
                    d1 -=1
                    continue
                    
                if s[i] == 'R' and d1 > 0:
                    rban += 1
                elif s[i] == 'D' and r1 > 0:
                    dban += 1
                    
                
                
            
            if r1 and not d1:
                return "Radiant"
            elif d1 and not r1:
                return "Dire"