class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        
        s = ''
        while k >= (n - len(s)) + 26:
            s+= 'z'
            k -= 26
        
        char = chr(k - (n-len(s)) + ord('a'))
        s += char
        k -= k - (n-len(s))
        s += 'a' * k
        
        
        
        return s[::-1]