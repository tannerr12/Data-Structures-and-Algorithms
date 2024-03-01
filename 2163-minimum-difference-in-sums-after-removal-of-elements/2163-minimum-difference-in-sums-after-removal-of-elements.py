class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        
        #left - mid - right
        
        #1,6,3  5,7,8  4,3,1
        
        #remove a number from mid
        #remove a number from left but add the leftmost number to left from mid
        #remove a number from right but add the rightmost number to right
        
        #starting 10, 20, 8
        
        #6-5 = 1
        #8 - 1 = 7
        #we take the 7
        
        #1,6,3, 5,7, 8,4,3
        
        #6 - 5 = 1
        #7 - 3 = 4
        
        #1,6,3, 5, 7,8,4
        
        #6-5
        #5-4  either or
        
        #1,3,5, 7, 8 ,4 = 9 - 19 = -10

        target = len(nums) //3 
        heap = []
        total = 0
        res = float('inf')
        
        ans = [[0 for j in range(2)] for i in range(len(nums))]
        
        for i in range(len(nums)):
            heappush(heap, -nums[i])
            total += nums[i]
            
            while len(heap) > target:
                val = heappop(heap)
                val = -val
                total -= val
            
            if len(heap) == target:
                ans[i][0] = total
        
        heap = []
        total = 0
        for i in range(len(nums)-1,-1,-1):
            if len(heap) == target:
                ans[i][1] = total
                
            heappush(heap, nums[i])
            total += nums[i]
            
            while len(heap) > target:
                val = heappop(heap)
                total -= val
            
            if ans[i][0] == 0 or ans[i][1] == 0:
                continue
            
            res = min(res, ans[i][0] - ans[i][1])
        

        #print(ans)
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 