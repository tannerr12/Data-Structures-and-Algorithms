class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        counter = Counter()
        for ch in s: 
            counter[ord(ch) - ord('a')]+=1
        
        for i in range(26):
            for j in range(26):
                
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue
                
                #get the character values
                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                majorCount = 0
                minorCount = 0
                
                restMinor = counter[j]
                
                for ch in s:
                    
                    if ch == major:
                        majorCount += 1
                    
                    if ch == minor:
                        minorCount += 1
                        restMinor -= 1
                    
                    if minorCount > 0:
                        res = max(res, majorCount - minorCount)
                    
                    if majorCount < minorCount and restMinor > 0:
                        majorCount = 0
                        minorCount = 0
                        
        
        return res
                
        
        
        