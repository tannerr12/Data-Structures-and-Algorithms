class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        
        '''
        
        2-3 = 1
        3-1 = 2
        1-5 = 4
        5-4 = 1
        
        =     8
        
        reversing a subarray will not change anything internal to the subarray?
        
        before the internal was 2,4
        [2,5,1,3,4]
        
        after 4,2
        
        #the only impact is the outer edges to before
        1,1
        
        #after
        3,1
        
        
        #how do we find the value on the right end with the biggest difference to the number on the left and the number on the left end with the biggest number to the right?
        
        #at any integer we choose for left we must swap the number next to left
        
        #our problem is now how do we find the value on the right to swap and compare with our current number?
        
        '''

        maxi, mini = -math.inf, math.inf
        
        for a, b in zip(nums, nums[1:]):
            maxi = max(min(a, b), maxi)
            mini = min(max(a, b), mini)
        change = max(0, (maxi - mini) * 2)
        
        # solving the boundary situation
        for a, b in zip(nums, nums[1:]):
            tmp1 = - abs(a - b) + abs(nums[0] - b)
            tmp2 = - abs(a - b) + abs(nums[-1] - a)
            change = max([tmp1, tmp2, change])
			
        original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
        return  original_value + change