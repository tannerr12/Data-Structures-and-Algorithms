class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        #startwords does not contain a letter not in target
        #startwords is less than = len(target) -1 len
        #you only get one letter
        
        #can we group these words by length
        #bitmasks
        
        mp = defaultdict(int)
        
        for i,e in enumerate(startWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
        
            mp[mask] += 1
            
    
        #print(mp)
        
        res = 0
        for i,e in enumerate(targetWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
        
            for i in range(32):
                
                if mask & (1 << i) > 0:
                    mask ^= (1 << i)
                    if mask in mp:
                        res += 1
                        break
                    mask ^= (1 << i)
        
        return res
                
            