class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res = set()
        for i in range(len(s)):
            c = Counter()
            c[s[i]] += 1
            res.add(s[i])
            for j in range(i+1, len(s)):
                c[s[j]] += 1
                
                if min(c.values()) == max(c.values()):
                    res.add(s[i:j+1])
        
        
        return len(res)
                    
                
                