class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        n = len(nums)
        arr = []
        tags = {}
        for i in range(len(nums)):
            for num in nums[i]:
                arr.append([num, i])
                

        arr.sort()
        
        l = 0
        ans = []
        res = float('inf')
        for i in range(len(arr)):
            val,tag = arr[i]
            
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] += 1
            
            
            while len(tags) == n:

                if arr[i][0] - arr[l][0] < res:
                    res = arr[i][0] - arr[l][0]
                    ans = [arr[l][0],arr[i][0]]

                v,t = arr[l]
                tags[t] -=1
                if tags[t] == 0:
                    del tags[t]
                l+=1
            
        
        return ans