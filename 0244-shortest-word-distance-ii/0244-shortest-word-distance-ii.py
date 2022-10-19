class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        
        self.h = collections.defaultdict(list)
        for i in range(len(wordsDict)):
            w = wordsDict[i]
            self.h[w].append(i)
            
    def shortest(self, word1: str, word2: str) -> int:
        
        w1Arr = self.h[word1]
        w2Arr = self.h[word2]
        
        i,j = 0,0
        dist = float('inf')
        while i < len(w1Arr) and j < len(w2Arr):
            dist = min(dist,abs(w1Arr[i]-w2Arr[j]))
            
            if w1Arr[i] < w2Arr[j]:
                i +=1
            else:
                j +=1
        
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)