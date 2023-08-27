class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        
        
        #1,2,1,2,1,2,1
        #1,3,4,6,7,9,10
        
        
        #0 -> 1 2 - 3
        prefix = []
        prefix.append(0)
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        for i in range(1,len(nums)):
            left = prefix[i]
            seen = set()
            
            for j in range(i + 2, len(nums)-1):
                total = (prefix[j] - prefix[i+1])
                targetAmt = left * 2
                diff = total - targetAmt
                if diff in seen and prefix[-1] - prefix[j+1] == left:
                    return True
                
                if j > i + 2 and prefix[j-1] - prefix[i+1] == left:
                    seen.add(nums[j-1])

                
        
        return False
                