class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        cumSum, res = 0,0
        visited = {}
        
        for i in range(len(nums)):
            val = nums[i]
            
            if val == 0:
                cumSum -=1
            
            else:
                cumSum +=1
                
            
            
            
            
            if cumSum ==0:
                res = i +1
            
            elif cumSum in visited:
                res = max(res,i-visited[cumSum])
                
            
            else:
                visited[cumSum] = i
                
        
        
        return res
            
            
            
            