class Solution:
    def maxProduct(self, s: str) -> int:
        #idea can we use 26 bits and for each bit position = character palindrone = 0 non = 1 if prev palindrone and new len odd = palindrone if even bits = 0
        
        def isPalindrone(s):
            
            l,r = 0, len(s) -1
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            
            return True
                
        
        N = len(s)
        h= {}
        for mask in range(1, 1 << N):
            subset = ''
            for i in range(N):
                
                if mask & (1 << i) >= 1:
                    subset+= s[i]
                
            
            if len(subset) > 0 and subset == subset[::-1]:
                h[mask] = len(subset)
        
        
        #print(h)
        res = 0
        for h1 in h.keys():
            for h2 in h.keys():
                if h1 & h2 == 0:
                    res = max(res,h[h1] * h[h2])
        
        return res
                
                    
                
        