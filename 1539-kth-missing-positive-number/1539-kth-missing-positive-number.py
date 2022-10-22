class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
         
            
        a = [i for i in range(len(arr) + k)]
        
        
        l,r = 0, len(arr) -1
        
        
        while l<=r:
        
            
            
            curr = (l+r)// 2
            
            if arr[curr] - curr -1 < k:
                l = curr +1
                
            else:
                
                r = curr -1
        
        
        return l +k
            
        
        