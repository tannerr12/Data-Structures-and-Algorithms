class Solution:
    def lastStoneWeightII(self, heap: List[int]) -> int:
        heap.sort()
        
        #print(stones)
        
        @cache
        def dfs(i,tot):
            
            if i >= len(heap):
                if tot >= 0:
                    return tot
                else:
                    return float('inf')
            
            res = float('inf')
            
            res = min(res,dfs(i+1, tot - heap[i]), dfs(i+1, tot + heap[i]))
            
            return res
            
        
        return dfs(0,0)
                    
            