class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        #create a unique grouping of masks from starting words
        mp = set()
        for i,e in enumerate(startWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
            mp.add(mask) 

        #create the masks from targetWords but we need to find a match by removing 1 character from targetwords
        res = 0
        for i,e in enumerate(targetWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
         
            
            for i in range(26):
                if mask & (1 << i) > 0:
                    mask ^= (1 << i)
                    if mask in mp:
                        res += 1
                        break
                    mask ^= (1 << i)
        
        return res
                
            