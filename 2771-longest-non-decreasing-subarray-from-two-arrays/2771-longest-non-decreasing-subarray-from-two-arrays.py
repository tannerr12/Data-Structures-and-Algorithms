class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
    
        res = 0
        dp1, dp2 = 0,0
        for i in range(len(nums1)):
            #nums1 -> nums1
            t1 = dp1 + 1 if nums1[i-1] <= nums1[i] else 1
            #nums1 -> nums2
            t12 = dp1 + 1 if nums1[i-1] <= nums2[i] else 1
            
            #nums2 -> nums2
            t2 = dp2 + 1 if nums2[i-1] <= nums2[i] else 1
            #nums2 -> nums1
            t21 = dp2 + 1 if nums2[i-1] <= nums1[i] else 1
            
            dp1 = max(t21, t1)
            dp2 = max(t12, t2)
            
            res  = max(res, dp1,dp2)
            
        
        return res
        
        '''
        @cache
        def dfs(i,last):
            
            if i == len(nums1):
                return 0
            
            res = float('-inf')
            if last == float('-inf'):
                v1 = max(res, dfs(i+1, last))
                v2 = max(res,dfs(i+1, nums1[i])) + 1
                v3 = max(res,dfs(i+1, nums2[i])) + 1 
                res = max(res, v1,v2,v3)
            else:
                v1,v2 = 0,0
                if nums1[i] >= last:
                    v1 = max(res, dfs(i+1, nums1[i])) + 1
                
                if nums2[i] >= last:
                    v2 = max(res, dfs(i+1, nums2[i])) + 1
                
                res = max(res, v1,v2)
                
            
            return res
        
        return dfs(0,float('-inf'))
    
    
        def rec(i,prev):
            if(i==len(nums1)):
                return 0
            if(prev in dp[i]):
                return dp[i][prev]
            if(prev==-float('inf')):
                leave=rec(i+1,prev) #Leave if no element selected till now
                op1=1+rec(i+1,nums1[i]) #Take first element from nums1
                op2=1+rec(i+1,nums2[i]) #Take first element from nums2
                dp[i][prev]=max(leave,op1,op2) #Take max of above 3 options
                return dp[i][prev]
            else:
                op1=0
                op2=0
                if(nums1[i]>=prev):
                    op1=1+rec(i+1,nums1[i]) #Take elem from nums1
                if(nums2[i]>=prev):
                    op2=1+rec(i+1,nums2[i]) #Take elem from nums2
                dp[i][prev]=max(op1,op2)
                return dp[i][prev]
        dp=[{} for _ in range(len(nums1))]
        return rec(0,-float('inf'))