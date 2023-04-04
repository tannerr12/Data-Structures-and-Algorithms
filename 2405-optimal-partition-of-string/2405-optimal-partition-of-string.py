class Solution:
    def partitionString(self, s: str) -> int:
        
        letter = set()
        res = 1
        for char in s:
            
            if char in letter:
                letter = set()
                res += 1
            
            letter.add(char)
        
        return res 