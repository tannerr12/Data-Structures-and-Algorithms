class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        memo = {}
        def backtrack(i,temp):
            
            
            if (str(temp)) in memo:
                return 
            if len(temp) > 1:
            
                res.append(temp.copy())
               # return 
            
            
            
            memo[str(temp)] = True
            for i in range(i,len(nums)):

                if len(temp) == 0 or temp[-1] <= nums[i]:
                    
                    
                    temp.append(nums[i])
                    backtrack(i+1, temp)
                    temp.pop()
               


                
        backtrack(0,[])
        
        return res
            
            