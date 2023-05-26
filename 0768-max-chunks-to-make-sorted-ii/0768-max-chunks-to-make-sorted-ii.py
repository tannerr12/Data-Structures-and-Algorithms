class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        
        right = []
        left = []
        
        for i in range(len(arr)):
            
            if i == 0:
                left.append(arr[i])
            else:
                left.append(max(left[-1], arr[i]))
            
            
        for i in range(len(arr)-1,-1,-1):
            
            if i == len(arr)-1:
                right.append(arr[i])
                
            else:
                right.append(min(right[-1], arr[i]))
        
        
        right.reverse()
        
        res = 1
        for i in range(len(arr)-1):
            
            if  left[i] <= right[i+1]:
                res +=1
        
        return res
        
            

            
            