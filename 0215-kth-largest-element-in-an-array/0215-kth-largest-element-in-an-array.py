class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        
        k = len(nums) - k
        
        def quickSelect(l,r):
            
            p = l
            
            for i in range(l,r):
                
                if nums[r] >= nums[i]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            
            nums[p], nums[r] = nums[r], nums[p]
            
            if p == k:
                return nums[p]
            if k > p:
                return quickSelect(p+1,r)
            if k < p:
                return quickSelect(l,p-1)
                
        return quickSelect(0,len(nums) -1)