class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(i,temp,memo):
            
            for i in range(i,len(nums)):
                if not memo[i]:
                    memo[i] = True
                    temp.append(nums[i])
                    backtrack(i,temp,memo)
                    res.append(temp.copy())
                    temp.pop()
                    memo[i] = False

        
        backtrack(0,[],collections.defaultdict(bool))
        res.append([])
        return res
            
            
            