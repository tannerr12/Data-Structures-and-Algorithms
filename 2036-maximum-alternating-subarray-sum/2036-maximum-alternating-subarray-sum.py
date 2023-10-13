class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        
        prefix = [0]
        prefixAlt = [0]
        for i in range(len(nums)):
            if i % 2:
                prefix.append(prefix[-1] - nums[i])
                prefixAlt.append(prefixAlt[-1] + nums[i])
            else:
                prefix.append(prefix[-1] + nums[i])
                if i != 0:
                    prefixAlt.append(prefixAlt[-1] - nums[i])
        
        mxRight = [0] * len(prefix)
        mx = float('-inf')
        for i in range(len(prefix) -1,-1,-1):
            mx = max(mx, prefix[i])
            mxRight[i] = mx
            
        
        mxRight2 = [0] * len(prefixAlt)
        mx = float('-inf')
        for i in range(len(prefixAlt) -1,-1,-1):
            mx = max(mx, prefixAlt[i])
            mxRight2[i] = mx
            
            
        ans = float('-inf')
        
        
        #[3,-1,1,2]
        #[3,4,5,3]
        #[-1, -2, 0]
        #[1,-1]
        #[2]
        #[-3,-2,-1,-3]
        
        for i in range(0,len(prefix)-1,2):
            ans = max(ans, mxRight[i+1] - prefix[i])
        
        for i in range(0,len(prefixAlt)-1,2):
            ans = max(ans, mxRight2[i+1] - prefixAlt[i])
            
        return ans
            
        