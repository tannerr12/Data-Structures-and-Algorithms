class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        
        arr = []
        
        for x,y in zip(quality,wage):
            
            arr.append((y/x, x))
            
        
        arr.sort()
        heap = []
        
        total = 0
        res = float('inf')
        #print(arr)
        for i in range(len(arr)):
            ratio = arr[i][0]
            qual = arr[i][1]
            
            total += qual
            heappush(heap,-qual)
            if len(heap) > k:
                
                total += heappop(heap)
            
            if len(heap) == k:
                res = min(res, total * ratio)
            
        
        return res