class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mp = Counter(chars)
        res = 0
        for w in words:
            c = Counter(w)
            found = True
            for x,y in c.items():
                if mp[x] < y:
                    found = False
                    break
            
            if found:
                res += len(w)
        
        return res
                
                
            
            