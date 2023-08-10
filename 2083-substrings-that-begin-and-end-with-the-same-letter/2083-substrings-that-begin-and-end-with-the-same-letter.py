class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        nxt = [0] * len(s)
        cnt = defaultdict(int)
        for i in range(len(s)-1,-1,-1):    
            cnt[s[i]] += 1
            nxt[i] = cnt[s[i]]
        
        
        return sum(nxt)
            
            
            