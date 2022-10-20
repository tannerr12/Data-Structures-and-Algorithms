import random

class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums.copy()
        self.tempArr = nums.copy()
        
        
        
        

    def reset(self) -> List[int]:
        self.arr = self.tempArr.copy()
        return self.arr

    def shuffle(self) -> List[int]:
        
        samp = (random.sample(self.arr,len(self.tempArr)))
        for i in range(len(self.tempArr)):
            self.arr[i] = samp[i]
            
        
        return self.arr
            
        
        
        
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()