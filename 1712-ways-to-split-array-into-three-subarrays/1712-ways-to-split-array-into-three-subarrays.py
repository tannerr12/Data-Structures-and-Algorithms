class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        
        prefix = []
        prefix.append(0)
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        
        
        l = 1
        res = 0
        mid = 0
        for i in range(len(nums)-1):
            
            left = prefix[i+1]
            #right = prefix[-1] - prefix[i+1]
            mid = 0
            #idx = i+1
            
            #find mid ending point where we can start getting points
            #it should be atleast mid * 2
            midEnd = bisect_left(prefix, left * 2)
            if midEnd <= i+1:
                midEnd = i + 2
           # if midEnd >= len(prefix) -1 or left * 2 > prefix[-1] - (left * 2):
           #     break
            
            #how large can we make mid before end is too small
            target = ((prefix[-1] - prefix[i+1]) / 2) + prefix[i+1]
            
            
            midMax = bisect_right(prefix, target)
            
            if midMax >= len(prefix) -1 or prefix[midMax] - left > prefix[-1] - prefix[midMax]:
                midMax -=1
                if midMax == len(prefix)-1:
                    midMax -=1
            if midMax == i+1:
                continue
            
            res += max(midMax - midEnd +1, 0)
            res %= (10** 9 + 7)

        
        return res % (10 ** 9 + 7)