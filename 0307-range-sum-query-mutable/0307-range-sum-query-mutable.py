class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (len(nums) *2)
        self.n = len(nums)
        self.build(nums)
        
    def build(self, arr):
        
        for i in range(len(arr)):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[i*2] + self.tree[(i*2)+1]
        

    def update(self, index: int, val: int) -> None:
        #print(self.tree)
        index += self.n
        self.tree[index] = val
        index //=2
        while index >= 1:
            self.tree[index] = self.tree[index*2] + self.tree[(index*2)+1]
            index //= 2
        
        #print(self.tree)
    def sumRange(self, left: int, right: int) -> int:
        l,r = left, right
        l += self.n
        r += self.n
        r+=1
        total = 0
        
        while l < r:
            
            if l % 2:
                total += self.tree[l]
                l+=1
            
            if r % 2:
                r -=1
                total += self.tree[r]
        
            l //= 2
            r //= 2
        
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)