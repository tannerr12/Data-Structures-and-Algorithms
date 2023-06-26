class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        
        heap = []
        l,r = 0, len(costs) -1
        valsAdded = 0
        for i in range(candidates):
            if l == r:
                heapq.heappush(heap,(costs[l],l))
                valsAdded +=1
            else:
                heapq.heappush(heap,(costs[l],l))
                heapq.heappush(heap,(costs[r], r))
                valsAdded+=2
            l+=1
            r-=1
            if l > r:
                break
            
        r+=1
        l-=1
        #print(l,r)
        #print(heap)
        res = 0
        for i in range(k):
            
            val, idx = heapq.heappop(heap)
            
            if l >= r or valsAdded == len(costs):
                res += val
            elif idx <= l:
                l+=1
                heapq.heappush(heap,(costs[l], l))
                res += val
                valsAdded +=1
            else:
                r-=1
                heapq.heappush(heap,(costs[r], r))
                res += val
                valsAdded +=1
            
                
            
        return res