class Solution:
    def partitionString(self, s: str) -> int:
        
        letter = 0
        res = 1
        for char in s:
            v = ord(char) - ord('a')
            if letter & (1 << v):
                letter = 0
                res += 1
            
            letter |= (1 << v)
        
        return res 