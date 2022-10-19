class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        
        h = collections.defaultdict(list)
        
        for i, e in enumerate(wordsDict):
            
            h[e].append(i)
            
            
        
        
        wl1 = h[word1]
        wl2 = h[word2]
        dist = float('inf')
        
            
        i,j = 0,0
            
        while i < len(wl1) and j < len(wl2):
            if word1 == word2 and i == j:
                i+=1
                continue
            dist = min(dist, abs(wl1[i] - wl2[j]))
                
            if wl1[i] > wl2[j]:
                j +=1
                
            else:
                i +=1
            
            

        
        
        
        
        return dist