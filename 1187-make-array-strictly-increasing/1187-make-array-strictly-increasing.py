class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        
        arr2 = list(set(arr2))
        arr2.sort()
        
        @cache
        def dfs(i, last):
            
            if i >= len(arr1):
                return 0
            
            
            res = float('inf')
            
            #swap

            b = bisect_left(arr2, last + 1)
            

            if b < len(arr2) and b >= 0 and (arr1[i] > arr2[b] or arr1[i] <= last) and arr2[b] > last:
                res = min(res,dfs(i+1, arr2[b]) + 1)
            
            
            #dont swap
            if arr1[i] > last:
                res = min(res, dfs(i+1, arr1[i]))
            
            return res
        
        res = dfs(0,-1)
        
        return res if res != float('inf') else -1