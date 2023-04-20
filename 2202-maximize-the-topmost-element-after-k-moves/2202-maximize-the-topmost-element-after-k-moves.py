class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            return nums[0]
        #this will be k -1 moves
        left = nums[:k-1]
        mx = -1
        if left:
            mx = max(left)
        right = nums[k-1:]
        
        if right:
            if len(right) > 1 and right[1] > mx:
                return right[1]
            return mx
        
        else:
            k -= len(nums)
            
            if len(left) == 1 and k % 2 == 0:
                return -1
            if k:
                return mx
            else:
                return -1