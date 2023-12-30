class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        
        res = []
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i])
            
            if len(arr) == 3:
                if arr[-1] - arr[0] <= k:
                    res.append(arr)
                    arr = []
            
                else:
                    return []
        
        
        return res
            