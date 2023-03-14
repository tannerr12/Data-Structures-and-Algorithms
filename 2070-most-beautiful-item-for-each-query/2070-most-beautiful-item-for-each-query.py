class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        

        items.sort()
        mx = 0
        res = [0] * len(queries)
        
        for i in range(len(queries)):
            
            queries[i] = [queries[i], i]
            
        queries.sort()
        
        
        i = 0  
        
        for val,j in queries:
            
            while i < len(items) and items[i][0] <= val:
                mx = max(mx, items[i][1])
                i+=1
            
            res[j] = mx
            
        
        return res