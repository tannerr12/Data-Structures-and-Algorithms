class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        mp = set()
        found = set()
        for i,e in enumerate(startWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
            mp.add(mask) 

        
        res = 0
        for i,e in enumerate(targetWords):
            mask = 0
            for val in e:
                idx = ord(val) - ord('a')
                mask |= (1 << idx)
            
            if mask in found:
                res +=1
                continue
                
            for i in range(32):
                if mask & (1 << i) > 0:
                    mask ^= (1 << i)
                    if mask in mp:
                        found.add(mask ^ (1 << i))
                        res += 1
                        break
                    mask ^= (1 << i)
        
        return res
                
            