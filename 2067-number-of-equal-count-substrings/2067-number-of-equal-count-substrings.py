class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        mxUnique = len(set(s))
        res = 0
        mp = defaultdict(int)
        
        
        for i in range(1, mxUnique + 1):
            l= 0
            size = count * i
            over,equal = 0,0
            mp = defaultdict(int)
            for j in range(len(s)):
                if mp[s[j]] == count - 1:
                    equal += 1
                elif mp[s[j]] == count:
                    over += 1
                    
                mp[s[j]] += 1
                
                if j - l  >= size:
                    
                    if mp[s[l]] == count:
                        equal -= 1
                    elif mp[s[l]] == count + 1:
                        over -=  1
                    
                    mp[s[l]] -= 1
                    
                    l += 1
                    
                
                if equal == i and over == 0:
                    res += 1
        
        return res
                    
                    
                    
                    
        