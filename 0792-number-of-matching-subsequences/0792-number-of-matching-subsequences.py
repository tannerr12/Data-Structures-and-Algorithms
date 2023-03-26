class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        mp = defaultdict(dict)
        mp[len(s)-1][s[-1]] = len(s)-1
        for i in range(len(s) -2,-1,-1):
            
            for key,val in mp[i + 1].items():
                if key not in mp[i]:
                    mp[i][key] = val
            
            
            mp[i-1][s[i]] = i
        
        
        for key,val in mp[0].items():
            if key not in mp[-1]:
                mp[-1][key] = val
            
        mp[-1][s[0]] = 0
        
        #print(mp[2])
        res = 0
        for word in words:
            
            j = 0
            m = -1
            valid = True
            while j < len(word):
                char = word[j]
                if char in mp[m]:
                    j +=1
                    m = mp[m][char]
                else:
                    valid = False
                    break
                    
            if valid:
                res +=1
        
        return res