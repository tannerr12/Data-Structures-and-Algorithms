class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dnaMap = defaultdict(int)
        
        l = 0
        res = []
        for i in range(len(s)):
            
            
            while i - l + 1 > 10:
                
                l +=1
            
            
            if i - l + 1 == 10:
                st = s[l:i+1]
                dnaMap[st] +=1
                if dnaMap[st] == 2:
                    res.append(st)
        
        
        
        return res
        
       
        
            