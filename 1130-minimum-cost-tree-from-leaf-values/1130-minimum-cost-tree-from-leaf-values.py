class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @cache
        def divide(l,r):
            
            if l == r:
                return [arr[l],0] 
            
            
            res = [float('-inf'), float('inf')] 
            for i in range(l,r):
                
                r1,c1 = divide(i+1,r)
                r2,c2 = divide(l,i)
                
                if  (r1 * r2) + c1 + c2 < res[1]:
                    res = [max(r1,r2), (r1 * r2) + c1 + c2]
            
            return res
        
        
        return divide(0,len(arr)-1)[1]
                