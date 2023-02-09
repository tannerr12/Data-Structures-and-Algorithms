class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        
        stack = []
        last = defaultdict(int)
        
        for i,c in enumerate(s):
            
            last[c] = i
            
        bitmask = 0
        
        for i,c in enumerate(s):
            v1 = ord(c) - ord('a')
            if bitmask & (1 << v1) > 0:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                val = stack.pop()
                v2 = ord(val) - ord('a')
                bitmask ^= (1<<v2)
                
                
      
            stack.append(c)
       
            bitmask |= (1 << v1)
        
        return ''.join(stack)