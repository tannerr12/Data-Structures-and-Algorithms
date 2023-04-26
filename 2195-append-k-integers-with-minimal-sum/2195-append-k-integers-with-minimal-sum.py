class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = min((k * (k+1)) //2, (nums[0] - 1) * (nums[0]) //2)
        k-= min(k, nums[0] -1)
        
        for i in range(len(nums) -1):
            
            if k > 0 and nums[i] != nums[i+1]:
                if nums[i+1] - nums[i] > k:
                    res += ((nums[i] + k) * (nums[i] + k + 1) //2) - ((nums[i] * (nums[i] + 1)) //2) 
                    k = 0
                    break
                else:
                    res += ((nums[i+1] - 1) * (nums[i+1]) //2) - ((nums[i] * (nums[i] + 1)) //2) 
                    k -= nums[i+1] - nums[i] -1
       
            
        
        
        if k:
            res += ((nums[-1] + k) * (nums[-1] + k + 1) //2) - ((nums[-1] * (nums[-1] + 1)) //2) 
        return res