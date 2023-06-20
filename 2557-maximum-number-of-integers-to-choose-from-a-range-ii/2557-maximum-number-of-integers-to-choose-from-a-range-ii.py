class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = list(set(banned))
        banned.sort()
        prefix = []

        
        for i in range(len(banned)):
            if i == 0:
                prefix.append(banned[i])
            else:
                prefix.append(prefix[-1] + banned[i])
            
        start = -1
        end = -1
        found = False
        for i in range(len(banned)):
            if banned[i] > n:
                break
            b = prefix[i]
            left = (banned[i] * (banned[i] +1)) // 2
            left = left - b
            
            if left > maxSum:
                end = i
                break
            
            start = i
        
        
        #print(start)
        #print(end)
        
        # start -> 6 so we do 6 - (start + 1) = 2  
        # than we find the rest of the range between index start and end which could be bin search taking that sum + left

        #search between these 2 points
        leftSum = 0
        #leftCount = 0
        left = 0
        st = 0
        if start >= 0:
            st = banned[start]
            left = banned[start] + 1
            leftSum = (banned[start] * (banned[start] +1)) // 2
            leftSum = leftSum - prefix[start]
            #leftCount = banned[start] - (start + 1)
        
        right = n
        
        if end >= 0:
            right = banned[end] -1
        
        res = 0
        while left <= right:
            
            mid = (left + right) // 2
            
            calc = ((mid + (st + 1)) * (mid - (st + 1) + 1)) // 2
            
            if (calc + leftSum) > maxSum:
                right = mid -1
            else:
                res = mid - (start + 1)
                left = mid + 1
                
            
        return res if res != 0 else st - (start + 1)
        
        
        