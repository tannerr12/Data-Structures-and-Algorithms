class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (len(nums) *2)
        self.n = len(nums)
        self.build(nums)
        
    def build(self, arr):
        
        for i in range(len(arr)):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]
        

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        index >>= 1
        while index >= 1:
            self.tree[index] = self.tree[index << 1] + self.tree[(index << 1) | 1]
            index >>= 1
        
    def sumRange(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        r+=1
        total = 0
        
        while l < r:
            
            if l & 1:
                total += self.tree[l]
                l+=1
            
            if r & 1:
                r -=1
                total += self.tree[r]
        
            l >>= 1
            r >>= 1
        
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)