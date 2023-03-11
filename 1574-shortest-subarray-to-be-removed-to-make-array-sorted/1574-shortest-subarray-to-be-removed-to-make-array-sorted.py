class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        
        l,r = 0,len(arr)-1
        
        while l < len(arr):
            
            if l+1 == len(arr):
                return 0
            if arr[l] <= arr[l+1]:
                l+=1
            else:
                break
                l,r = 0,len(arr)-1
        
        tr = len(arr)-1
        while tr >= 0:
            
            if tr-1 == -1:
                return 0
            if arr[tr] >= arr[tr-1]:
                tr-=1
            else:
                break
        
        res = min(len(arr) - (l + 1), tr)
        prev = arr[r]
        while l >= 0 and arr[r] <= prev:
            
            while l >= 0 and arr[r] < arr[l]:
                l-=1
            while r >= l and arr[r] >= arr[l] and arr[r] <= prev:
                res = min(res, r - l-1)
                prev = arr[r]
                r -=1
                

            
            
            
            
            
           
        
        return res