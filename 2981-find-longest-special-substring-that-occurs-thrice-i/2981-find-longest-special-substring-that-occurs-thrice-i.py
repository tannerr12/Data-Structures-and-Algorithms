class Solution:
    def maximumLength(self, s: str) -> int:
        
        for i in range(len(s)-1,0,-1):
            mp = defaultdict(int)
            score = defaultdict(int)
            l = 0
            for j in range(len(s)):
                
                mp[s[j]] += 1
                
                if j - l + 1 == i:
 
                    if mp[s[j]] == j - l + 1:
                        score[s[j]] += 1
                        if score[s[j]] == 3:
                            return i
                    
                    mp[s[l]] -= 1
                    l += 1
        
        return -1
            
        