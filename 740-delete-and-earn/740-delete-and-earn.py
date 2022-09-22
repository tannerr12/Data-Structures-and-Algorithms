class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numsCheck = set(nums)
        h = Counter(nums)
        nums = list(numsCheck)
        nums.sort()
        
        
    
        earn1,earn2 = 0,0
        
        for i in range(len(nums)):
            
            curr = nums[i] * h[nums[i]]
            
            if i > 0 and nums[i] == nums[i-1] + 1:
                
                temp = earn2
                
                earn2 = max(curr + earn1, earn2)
                
                earn1 = temp
            else:
                
                
                temp  = earn2
                earn2 = curr + earn2
                
                earn1 = temp
            
        return earn2
    