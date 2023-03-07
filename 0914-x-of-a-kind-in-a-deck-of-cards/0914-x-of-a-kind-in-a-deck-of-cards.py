class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        deck = Counter(deck)
        #print(deck)
        start = min(deck.values())
        i = 2
        valid = False
        while i <= start:
        
            valid = True
            for key,val in deck.items():
                
                if val % i != 0:
                    valid = False
                    break
            
            
            if valid:
                return True
            
            i += 1 + i % 2
        
        return False
            