class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        odd,even = 0,0
        
        for i,e in enumerate(nums):
            if i % 2:
                odd += e
            else:
                even += e
        
       # print(odd)
       # print(even)
        oddRight = 0
        evenRight = 0
        res = 0
        for i in range(len(nums) -1,-1,-1):
            
            if i % 2:
                odd -= nums[i]
            else:
                even -= nums[i]
            
            
            if odd + oddRight == even + evenRight:
                res +=1
            
            if i % 2:
                evenRight += nums[i]
            else:
                oddRight += nums[i]
                
        
        return res