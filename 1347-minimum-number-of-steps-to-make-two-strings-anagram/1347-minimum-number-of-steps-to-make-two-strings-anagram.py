class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        t1 = Counter(s)
        t2 = Counter(t)
        
        
        diff = 0
        
        for i in range(26):
            
            char = chr(i + ord('a'))
            
            if t2[char] > t1[char]:
                diff += t2[char] - t1[char]
        
        return diff
        