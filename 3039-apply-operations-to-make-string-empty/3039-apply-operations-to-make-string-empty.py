class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
        c = Counter(s)
        mx = max(c.values())
        
        ans = []
        
        for i in range(len(s)-1,-1,-1):
            
            if c[s[i]] == mx:
                ans.append(s[i])
                c[s[i]] = 0
        
        
        ans = ans[::-1]
        
        return ''.join(ans)