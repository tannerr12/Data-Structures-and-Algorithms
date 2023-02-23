class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #capital needed first
        
        heap = []
        res = 0
        arr = []
        
        for p,c in zip(profits,capital):
            arr.append((c, p))
        
        arr.sort()
        #print(arr)
        i = 0
        while i < len(arr) and k:
            while i < len(arr) and arr[i][0] <= w:
                heappush(heap,-arr[i][1])
                i+=1
            
            if heap:
                val = heappop(heap)
                val = -val
                w += val
                k-=1
            else:
                return w
        
        
        while k and heap:
            val = heappop(heap)
            val = -val
            w += val
            k-=1
            
        return w
            