class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        
        h = Counter(words)
        
        
        arr = []
            
        
        
        for x,y in h.items():
            
            heapq.heappush(arr,(-y,x))
            
        
        
        res = []
        
        while k != 0:
            x,y = heapq.heappop(arr)
            
            res.append(y)
            k-=1
        
       
       
        
        return res