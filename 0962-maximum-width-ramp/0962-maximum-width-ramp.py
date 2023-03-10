class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        mono = []
        
        for i,n in enumerate(nums):
            mono.append([n,i])
        
        mono.sort()
        
        prefix = []
        
        for i in range(len(mono)):
            
            if i == 0:
                prefix.append(mono[i][1])
            
            else:
                prefix.append(min(prefix[-1], mono[i][1]))
        
        
        #print(mono)
        #print(prefix)
        res = 0
        for i in range(len(mono)-1,0,-1):
            res = max(res,mono[i][1] - prefix[i-1])
        
        return res