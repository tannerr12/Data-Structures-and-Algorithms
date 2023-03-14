class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #anytime our running total can stay >= 0 we should keep it
        #we should also keep track of our biggest negative to remove it from sum when we see a negative
        
        
        res = 0
        
        noskip = 0
        skip = 0
        allneg = True
        mxneg = float('-inf')
        for i in range(len(arr)):
            if arr[i] >=0:
                allneg = False
            else:
                mxneg = max(arr[i],mxneg)
            skip = max(noskip, skip + arr[i])
            noskip = max(noskip + arr[i],arr[i])
            res = max(res, skip,noskip)
            
        
        return res if allneg == False else mxneg