class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        letter = defaultdict(int)
        
        for i in range(len(order)):
            letter[order[i]] = i
        
        for i in range(1,len(words)):
            found = False
            for j in range(min(len(words[i-1]), len(words[i]))):
                
                v1 = letter[words[i][j]]
                v2 = letter[words[i-1][j]]
                
                if v1 < v2:
                    return False
                elif v2 < v1:
                    found = True
                    break
                
                
            if not found and len(words[i]) < len(words[i-1]):
                return False
            
                

                
                
                        
        
        return True
                