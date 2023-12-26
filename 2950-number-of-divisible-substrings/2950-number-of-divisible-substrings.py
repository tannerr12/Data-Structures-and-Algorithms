class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        def getCharVal(x):
            v = ord(x) - ord('a') + 1
            
            if v == 1 or v == 2:
                return 1
            
            else:
                return (v // 3) + 1
            

        prefix = []
        prefix.append(0)

        for i, val in enumerate(word):
            prefix.append(prefix[-1] + getCharVal(val))

        res = 0
        for i in range(0, len(word) + 1):
            
            for j in range(0, len(word) - i, 1):
                val = prefix[j + i + 1] - prefix[j]
                if val % (i + 1) == 0:
                    res +=1
    
        return res 
                    
                
                
                
            