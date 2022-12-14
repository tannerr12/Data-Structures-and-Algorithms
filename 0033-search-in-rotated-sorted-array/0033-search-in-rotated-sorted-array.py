class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums) -1

        pivot = -1
        while l <= r:
           
            curr = (l+r)//2

            if (curr < len(nums) -1 and nums[curr] > nums[curr +1]):
                pivot = curr +1
                break
            if nums[curr] < nums[curr -1]:
                pivot = curr
                break
            elif nums[curr] > nums[r]:
                l = curr +1
            else:
                r = curr - 1
            
            
        
        newArr = nums[pivot:] + nums[0:pivot]

        l,r = 0,len(nums) -1
        
        
        while l <= r:
           
            curr = (l+r)//2
            
            if newArr[curr] == target:
                return (curr + pivot) % len(nums)
            
            elif newArr[curr] > target:
                r = curr -1
            else:
                l = curr + 1
            
        
            
        
        return -1