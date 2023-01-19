class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        
        zero = s.count('0')
        
        
        ones = 0
        val = 0
        for i in range(len(s) -1,-1,-1):
            
            if s[i] == '1':
                
                base = 2 ** (len(s) - 1 - i)
                
                if val + base <= k:
                    ones +=1
                    val += base
                else:
                    break
        
        
        return ones + zero
        