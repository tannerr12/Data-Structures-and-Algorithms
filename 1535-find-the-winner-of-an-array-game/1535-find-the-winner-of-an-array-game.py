class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        #2,1,3,5,4,6,7
        
        
        #5
        

        count = 0
        mx = arr[0]
        
        for i in range(1,len(arr)):
            
            if mx > arr[i]:
                count += 1
            
            else:
                mx = arr[i]
                count = 1
            
            if count >= k:
                return mx
        
        
        return mx
                
            