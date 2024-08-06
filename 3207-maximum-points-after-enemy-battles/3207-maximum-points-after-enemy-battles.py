class Solution:
    def maximumPoints(self, enemyEnergies: List[int], ce: int) -> int:
        
        heapb = []
        heaps = []
        marked = set()
        for i in range(len(enemyEnergies)):
            e = enemyEnergies[i]
            heappush(heapb, (-e, i))
            heappush(heaps, (e, i))
            
        
        res = 0
        
        while heaps:
            
            while heaps and heaps[0][1] in marked:
                heappop(heaps)
            
            while heapb and heapb[0][1] in marked:
                heappop(heapb)
            
            
            while heapb and ce < heaps[0][0] and res > 0:
                
                val,pos = heappop(heapb)
                if pos in marked:
                    continue
                
                marked.add(pos)
                ce += -val
            
            while heaps and heaps[0][1] in marked:
                heappop(heaps)
                
            if heaps and ce >= heaps[0][0]:
                mx = ce // heaps[0][0]
                ce -= heaps[0][0] * mx
                res += mx
            
            if res == 0:
                return 0
        
        return res
                