class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        ls = []
        ls.append([k,nums[0]])
        run = -nums[0]
        for i in range(len(nums)):
            while ls and ls[0][0] == i:
                run += heappop(ls)[1]
            newnum = nums[i] + run
            if newnum < 0 or (newnum > 0 and i + k > len(nums)):
                return False
            else:
                if newnum > 0:
                    heappush(ls, [i + k, newnum])
                    run -= newnum
        
        return True
                    
            
        
        
        

        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        