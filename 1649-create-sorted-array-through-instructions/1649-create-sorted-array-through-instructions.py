class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        nums = []
        cost = 0
        MOD = 10 ** 9 + 7
        for i in range(len(instructions)):
            
            insort(nums, instructions[i])
            
            left = bisect_left(nums, instructions[i])
            right = bisect_right(nums, instructions[i])
            
            cost = (cost + min(left, (len(nums) - right))) % MOD
        
        
        return cost