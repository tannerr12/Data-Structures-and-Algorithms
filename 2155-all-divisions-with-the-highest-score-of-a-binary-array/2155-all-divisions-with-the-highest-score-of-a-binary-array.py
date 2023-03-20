class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        
        p = []
        p.append(0)
        for i in range(len(nums)):
            
            p.append(nums[i] + p[-1])
            
        
        #p.append(p[-1])
        
        res = []
        mxScore = 0
        
        
        for i in range(len(p)):
            
            right = p[-1] - p[i]
            left = i - (p[i] - p[0])
            score = left + right 
            
            if score > mxScore:
                mxScore = score
                res = [i]
            elif score == mxScore:
                res.append(i)
        
        return res