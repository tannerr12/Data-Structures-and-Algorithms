class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        ls = []
        
        for key,val in c.items():    
            ls.append(val)
        
        ls.sort()
        mx = ls[0] + k
        mn = ls[0]
        
        ans = float('inf')
        deleted = 0
        for i in range(len(ls)):
            res = deleted
            mn = ls[i]
            mx = mn + k
            for j in range(i, len(ls)):
                if ls[j] > mx:
                    res += ls[j] - mx
                    
            ans = min(ans, res)
            deleted += ls[i]
        return ans
        
        
        
            
            
        