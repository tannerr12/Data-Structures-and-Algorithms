class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        h = Counter(words)
        
        
        arr = []
            
        
        
        for x,y in h.items():
            
            heapq.heappush(arr,(-y,x))
            
        
        
        res = []
        
        while k != 0:
            x,y = heapq.heappop(arr)
            
            res.append((x*-1,y))
            k-=1
        
        sorted(res, key=lambda x: (-x[0], x[1]))
        print(res)
        
        finalRes = []
        
        for x,y in res:
            
            finalRes.append(y)
            
        
        
        return finalRes