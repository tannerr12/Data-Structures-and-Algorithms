from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        
        
        def merge(nums):
            
            if len(nums) <= 1:
                return nums
            
            left = merge(nums[:len(nums) //2])
            right = merge(nums[len(nums) //2:])
            
            
            return partition(left,right)
        
        
        
        
        res = 0 
        def partition(left,right):
            nonlocal res
            l,r = 0,0
            
            i,j = 0,0
            arr = []
            
            
            for i in range(len(left)):
                
                while j < len(right) and left[i] > right[j] * 2:
                    j+=1
      
                res += j        
        
            while l < len(left) and r < len(right):
                

                if left[l] <= right[r]:
                    arr.append(left[l])
                    l+=1
                
                else:
                    arr.append(right[r])
                    r+=1
            
                
                
            arr.extend(right[r:])
            arr.extend(left[l:])
                
            return arr
        
        
        merge(nums)
        return res
                    