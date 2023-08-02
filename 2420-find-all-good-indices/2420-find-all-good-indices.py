class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        stack = []
        
        decrease = [0] * len(nums)
        decreaseRev = [0] * len(nums)
        for i in range(len(nums)):
            
            if stack and nums[i] > nums[stack[-1]]:
                while stack:
                    idx = stack.pop()
                    decrease[idx] = i 
            
            stack.append(i)
        
        
        while stack:
            idx = stack.pop()
            decrease[idx] = len(nums) -1
        
        
        for i in range(len(nums)-1,-1,-1):
            
            if stack and nums[i] > nums[stack[-1]]:
                while stack:
                    idx = stack.pop()
                    decreaseRev[idx] = i 
            
            stack.append(i)
            

        
        while stack:
            idx = stack.pop()
            decreaseRev[idx] = 0
        #print(decrease)
        #print(decreaseRev)
        
        res = []
        for i in range(k, len(nums) - k):
            
            if decreaseRev[i+k] <= i and decrease[i-k] >= i:
                res.append(i)
                
        return res