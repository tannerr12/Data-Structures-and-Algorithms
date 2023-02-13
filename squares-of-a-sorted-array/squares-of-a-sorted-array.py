class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        arr = []
        
        zeropos = -1
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                zeropos = i
                break
        
        #gather right of 0
        #gather left of 0
        #merge sort
        
        revArr = []
        forArr = []
        if zeropos == -1:
            zeropos = len(nums)
        for i in range(zeropos-1,-1,-1):
            revArr.append(nums[i] ** 2)
        

        for i in range(zeropos, len(nums)):
            forArr.append(nums[i] ** 2)
            

        l,r = 0 , 0
        while l < len(revArr) and r < len(forArr):
            
            if revArr[l] <= forArr[r]:
                arr.append(revArr[l])
                l+=1
            
            else:
                arr.append(forArr[r])
                r +=1
        
        
        while l < len(revArr):
            arr.append(revArr[l])
            l+=1
        while r < len(forArr):
            arr.append(forArr[r])
            r+=1
        
        return arr
        