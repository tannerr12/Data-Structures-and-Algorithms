class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        resMemo = set()
        def backtrack(i,temp,memo):
            
            if len(temp) == len(nums):
                
                s = ''.join(str(n) for n in temp)
                if s not in resMemo:
                   
                    resMemo.add(s)

                    res.append(temp.copy())
                return
            
            
            for i in range(len(nums)):
                if i in memo and memo[i]:
                    continue
                
                memo[i] = True
                temp.append(nums[i])
                
                backtrack(i,temp,memo)
                
                temp.pop()
                memo[i] = False
                
                
        
        backtrack(0,[], {})
        
        #print(res)
        return res