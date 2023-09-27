class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        ls = deque([[k,nums[0]]])
        run = -nums[0]
        
        for i in range(len(nums)):
            if ls and ls[0][0] == i:
                run += ls.popleft()[1]
                
            newnum = nums[i] + run
            if newnum < 0 or (newnum > 0 and i + k > len(nums)):
                return False
            else:
                if newnum > 0:
                    ls.append([i + k, newnum])
                    run -= newnum
        
        return True
                    
            
        
        
        

        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        