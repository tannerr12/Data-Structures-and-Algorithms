class Solution:
    def longestPalindrome(self, s: str) -> str:

        new_s = '#'.join('^{}$'.format(s))
        len_s = len(new_s)
        P = [0] * len_s
        C = R = 0
        
        
        for i in range(1, len_s-1):
            if R > i:
                P[i] = min(R-i, P[2*C - i])
                
            #attempt to expand the palindrome centered at i
            while new_s[i+1+P[i]] == new_s[i-1-P[i]]:
                P[i] += 1
            #if palindrome centered at i expands pats R,
            #adjust center based on expanded palindrome
            if i + P[i] > R:
                C,R = i, i + P[i]
            
            
        #find the maximum element in P
        max_len = max(P)
        
        center_index = P.index(max_len)
        
        return s[(center_index  - max_len)//2: (center_index  + max_len)//2]
        
        