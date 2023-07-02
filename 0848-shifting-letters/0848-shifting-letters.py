class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        res = []
        newShift = []
        for i in range(len(shifts)-1,-1,-1):
            if i == len(shifts) -1:
                newShift.append(shifts[i])
            else:
                newShift.append(newShift[-1] + shifts[i])
        
        newShift.reverse()
        for x,y in zip(s, newShift):
            
            y %= 26
            pos = (ord(x) - ord('a') + y) % 26
            res.append(chr(pos + ord('a')))
        
        
        return ''.join(res)
            
            