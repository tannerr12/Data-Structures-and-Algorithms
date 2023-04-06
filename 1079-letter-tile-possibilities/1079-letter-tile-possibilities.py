class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        
        s = set()
        
        def comb(i, bitmask,word):
            
            if bitmask and word not in s:
                s.add(word)
                
            if i >= len(tiles):
                return
            
            
            for j in range(len(tiles)):
                if bitmask & (1 << j):
                    continue
                
                comb(i+1, bitmask | (1<<j),word + tiles[j])
                
            
        
        comb(0,0,'')
        
        #print(s)
        return len(s)
            