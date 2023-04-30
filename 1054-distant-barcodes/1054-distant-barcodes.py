class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        c = Counter(barcodes)
        res = []
        
        heap = []
        
        for key,val in c.items():
            heap.append([-val, key])
            
        
        heapify(heap)
        
        while heap:
            
            v1,k1 = heappop(heap)
            if not heap:
                res.append(k1)
                break
            
            v2,k2 = heappop(heap)
            
            res.append(k1)
            res.append(k2)
            
            if v1 + 1 != 0:
                heappush(heap, [v1 + 1, k1])
            if v2 + 1 != 0:
                heappush(heap,[v2 + 1, k2])
            
        
        
        return res