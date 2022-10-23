class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        def backtrack(s,e,turn):
            
            
            if s == e:
                return turn * nums[s]
            
            if (s,e) in memo:
                return memo[(s,e)]
            a = turn * nums[s] + backtrack(s+1,e, -turn)
            
            
            b = turn * nums[e] + backtrack(s,e -1, -turn)
            
            
            memo[(s,e)] = turn * max(turn * a, turn * b)
                
            return memo[(s,e)]
            
            
        
        
        
        return backtrack(0,len(nums) -1,1) >= 0