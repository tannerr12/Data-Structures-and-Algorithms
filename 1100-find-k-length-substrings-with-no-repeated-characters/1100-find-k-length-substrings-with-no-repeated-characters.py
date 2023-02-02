class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        l = 0
        h = {}
        res = 0
        for i in range(len(s)):
            


                while s[i] in h or i - l +1 > k:
                    h[s[l]] -=1
                    if h[s[l]] == 0:
                        del h[s[l]]
                    l+=1
                
                

                h[s[i]] = 1
                if i - l + 1 == k:
                    res +=1
                    
        
        return res
            
        