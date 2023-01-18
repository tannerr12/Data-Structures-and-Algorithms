class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def scan(arr):
            
            dp = []
            ls = []
            for i in range(len(arr)):
                
                idx = bisect_left(ls, arr[i])
                
                if len(ls) > idx:
                    ls[idx] = arr[i]
                else:
                    ls.append(arr[i])
                
                dp.append(len(ls))
            
            return dp
        

                    
        left = scan(nums)
        right = scan(nums[::-1])
                
        
        res = 0
        n = len(nums)
        for i in range(1,len(nums)-1):
            
            if left[i] > 1 and right[n-i-1] > 1:
                res = max(res,left[i] + right[n-i-1]-1)
        
        
        return n - res