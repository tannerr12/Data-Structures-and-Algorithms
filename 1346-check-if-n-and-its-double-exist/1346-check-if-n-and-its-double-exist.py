class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        
        #arr.sort()
        
        h = set()
        arr1 = set(arr)
        if 0 in arr1:
            count = 0
            for val in arr:
                if val == 0:
                    count +=1
            if count > 1:
                return True
        for val in arr1:

            if val * 2 in h or val in h:
                return True
            
            h.add(val * 2)
            h.add(val)
        return False
            
        
        
        seen =set(arr)
        
        l,r = 0, len(arr)-1
        
        
        while l <= r:
            
            curr = (l+r) // 2
            
            if arr[curr] * 2 in seen:
                return True
            
            if arr[curr] * 2 > arr[-1]:
                r = curr -1
                
            else:
                l = curr + 1
        
        
        
        return False
            