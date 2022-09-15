class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        def reverse(i):
            j = len(nums)-1
            
            while i < j:
                
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
                j-=1
                
                
        i,j = len(nums)-1, len(nums) -1
        
        while i > 0 and nums[i] <= nums[i -1]:
            i-=1
        
        if i == 0:
            nums.reverse()
            return
        
        else:
                k = i-1
                while nums[k] >= nums[j]:
                    j-=1
                    
                #swap
                nums[j],nums[k] = nums[k],nums[j]
        
                reverse(k + 1)
        
     
        