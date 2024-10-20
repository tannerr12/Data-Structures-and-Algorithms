class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
        res = 0
        l = 0
        count = defaultdict(int)
        for i in range(len(s)):
            
            count[s[i]] += 1
            
            while count[s[i]] >= k:
                
                res += len(s) - i
                count[s[l]] -= 1
                l += 1
        
        
        return res
                