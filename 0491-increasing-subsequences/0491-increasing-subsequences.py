class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        memo = {}
        def backtrack(i,temp,size,prev):
            
            
            if (temp) in memo:
                return 
            if size > 1:
            
                res.append(temp.split(','))
               # return 
            
            
            
            memo[(temp)] = True
            for i in range(i,len(nums)):

                if len(temp) == 0:
                    
                    backtrack(i+1, str(nums[i]), size +1,nums[i])
                    
                elif prev <= nums[i]:
                     backtrack(i+1, temp + ',' + str(nums[i]), size +1,nums[i])


                #backtrack(i+1,temp)
                
        backtrack(0,'',0,0)
        
        return res
            
            