class Solution:
    def numSplits(self, s: str) -> int:
        
        
        right = Counter(s)
        left = set()
        
        res = 0
        for i in range(len(s)):
            
            left.add(s[i])
            right[s[i]] -=1
            if right[s[i]] == 0:
                del right[s[i]]
            
            if len(left) == len(right):
                res +=1
        
        
        return res
            
            
            
        