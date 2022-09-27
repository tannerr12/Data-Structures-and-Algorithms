class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        tempres = []
        
        def dfs(k, start , target):
            if k != 2:
                for i in range(start, len(nums) - k +1):
                    if i > start and nums[i-1] == nums[i]:
                        continue

                    tempres.append(nums[i])
                    dfs(k-1, i+1, target - nums[i])
                    tempres.pop()
                return

            
            
            l,r = start, len(nums) -1
            while l < r:
                
                if nums[l] + nums[r] > target:
                    r -=1
                elif nums[l] + nums[r] < target:
                    l +=1
                else:
                    
                    res.append(tempres + [nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                            l+=1
            
                
            
            
        
                                                     
        dfs(4,0,target)
        return res
                
                
                
                
            