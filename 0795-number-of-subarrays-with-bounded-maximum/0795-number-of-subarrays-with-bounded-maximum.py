class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        #large numbers are walls nothing can be connected past them
        #small numbers need to be paired with a vaild number
        #valid numbers work with anything except large numbers
        
        arr = [[0,0]] * len(nums)
        
        lastL = len(nums)
        lastS = len(nums)
        lastM = len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= left and nums[i] <= right:
                lastM = i
                arr[i] = [0, lastM, lastL]
            elif nums[i] < left:
                lastS = i
                arr[i] = [1, lastM, lastL]
            else:
                lastL = i
                arr[i] = [2, lastM, lastL]
        
        res = 0
        for i in range(len(arr)):
            
            if arr[i][0] == 0:
                res += arr[i][2] - i 
            
            elif arr[i][0] == 1:
                if arr[i][2] > arr[i][1]:
                    res += arr[i][2] - i 
                    res -= arr[i][1] - i
        
        return res
                
            
            