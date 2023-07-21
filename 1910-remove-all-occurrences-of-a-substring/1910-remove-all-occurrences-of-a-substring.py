class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        found = True
        while found:
            found = False
            for i in range(len(part)-1, len(s)):
                if s[i-len(part)+1:i+1] == part:
                    s = s[:i - len(part)+1] + s[i+1:]
                    found = True
                    break
        
        return s
                