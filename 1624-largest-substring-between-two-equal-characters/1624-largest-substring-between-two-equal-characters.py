class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last = {}
        res = -1
        for i, char in enumerate(s):
            
            if char in last:
                res = max(res, i - last[char] - 1)
            else:
                last[char] = i
        
        return res
                