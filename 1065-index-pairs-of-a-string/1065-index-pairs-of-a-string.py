class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(len(text)):
            
            for w in words:
                if text[i:i+len(w)] == w:
                    pairs.append([i,i+len(w)-1])
                    
        
        
        pairs.sort()
        
        return pairs
                