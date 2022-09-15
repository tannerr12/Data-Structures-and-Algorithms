class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        resMemo = set()
        def backtrack(temp,counter):
            
            if len(temp) == len(nums):
                    
                res.append(temp.copy())
                return
            
            
            for num in counter:
                if counter[num] > 0:
                    
                
                    counter[num] -=1
                    temp.append(num)

                    backtrack(temp,counter)

                    temp.pop()
                    counter[num] +=1

                
        
        backtrack([],Counter(nums))
        
        #print(res)
        return res