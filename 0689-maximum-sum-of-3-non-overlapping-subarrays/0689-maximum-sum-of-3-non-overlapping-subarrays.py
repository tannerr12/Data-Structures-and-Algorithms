class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        #nums = [1] * (10**4 * 2)
        #k=100
        prefix = []
        prefix.append(0)
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        
        cand = {}
        
        for i in range(len(prefix)-k):
            cand[i] = prefix[i+k] - prefix[i]
        
        #print(cand)
        #{0: 3, 1: 3, 2: 3, 3: 8, 4: 13, 5: 12, 6: 6}
        
        #3, 3, 6, 8, 19... 
        
        
        @cache
        def dfs(i,left):
            if left == 0:
                return 0, []
            
            if i >= len(cand):
                return float('-inf'), []

            #take num

            takecurrSum, takeCurrIdx = dfs(i+k, left -1)
            takecurrSum += cand[i]
            

            #skip num
            skipcurrSum, skipCurrIdx = dfs(i+1,left)
            
            if takecurrSum >= skipcurrSum:
                return (takecurrSum, ([i] + takeCurrIdx)) 
            else:
                return (skipcurrSum, skipCurrIdx)    
            
        
        
        res = dfs(0,3)
        return res[1]
    
          
   