class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        cow,bull = 0,0  
        h = Counter(secret)
        
        for i in range(len(secret)):
            
            
            if secret[i] == guess[i]:
                bull +=1
                if h[secret[i]] == 0:
                    cow -=1
                else:
                    h[secret[i]] -=1
                
            
            elif guess[i] in h and h[guess[i]] > 0:
                cow+=1
                h[guess[i]] -=1
            
            
        
        
        return str(bull) + 'A' + str(cow) + 'B'