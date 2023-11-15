class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
    
        dpright = [0] * len(s)
        right = 0
        left = 0
            
        
        for i in range(len(s)-1,-1,-1):
            
            dpright[i] = right
            right |= (1 << (ord(s[i]) - ord('a')))
        
        
        def hammingDistance(x):
            count = 0
            while x:
                x -= x & -x
                count += 1
            
            return count
        
        chrBest = defaultdict(int)
        
        
        for num in range(len(s) -1):
            right = dpright[num]
            overlap = left & right
            #c = hammingDistance(overlap)
            chrBest[s[num]] |= overlap
            left |= (1 << (ord(s[num]) - ord('a'))) 
        
        
        
        total = 0
        
        for key,val in chrBest.items():
            total += hammingDistance(val)
        
        return total
            
                    
            
