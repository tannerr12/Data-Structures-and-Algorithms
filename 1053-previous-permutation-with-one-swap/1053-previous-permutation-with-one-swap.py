class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        mn = float('inf')
        hasSmaller = [False] * len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > mn:
                hasSmaller[i] = True
            
            mn = min(mn,arr[i])
        
        
        #print(hasSmaller)
        
        #furthest number to the right which is smaller 
        pos = -1
        for i in range(len(arr)-1,-1,-1):
            if hasSmaller[i]:
                pos = i
                break
        
        
        if pos == -1:
            return arr
        
        cur,posj = -1,-1
        
        for j in range(pos+1, len(arr)):
            if arr[j] < arr[pos]:
                if arr[j] > cur:
                    posj = j
                    cur = arr[j]
        
        arr[pos],arr[posj]= arr[posj],arr[pos]
        return arr
    
                