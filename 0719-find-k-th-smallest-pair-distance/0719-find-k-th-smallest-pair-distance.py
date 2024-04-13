class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        largest = nums[-1] - nums[0]
        largestK = n * (n-1) // 2
        
        #print(largestK)
        
        
        def isGood(mid):
            r = 1
            count = 0
            for l in range(len(nums)):
                while r < len(nums) and (r == l  or nums[r] - nums[l] <= mid):
                    r +=1

                if r < len(nums) and nums[r] - nums[l] == mid:
                    found = True
                count += r - l - 1
            
            
            return count >= k
            
        
        l,r = 0, largest
        a = -1
        while l <= r:
            
            mid = (l+r) // 2
            
            ans = isGood(mid)
          
            
            if ans:
                r = mid - 1
            else:
                l = mid + 1

        return l
    
  
