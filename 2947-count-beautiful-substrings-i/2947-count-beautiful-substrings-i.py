class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        vowel = ['a','e','i','o','u']
        res = 0
        for i in range(len(s)): 
            v,c = 0,0
            if s[i] in vowel:
                v +=1
            else:
                c +=1
            
            
            for j in range(i + 1, len(s)):

                if s[j] in vowel:
                    v +=1
                else:
                    c +=1
                
                if v == c and (v * c) % k == 0:
                    res += 1
                    
        
        return res
                