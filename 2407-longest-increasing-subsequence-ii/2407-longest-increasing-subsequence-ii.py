class SegmentTree:
    def __init__(self,array):
        self.n = len(array)
        self.max_tree = [0] * (self.n << 1)
        self.build_tree(array)
    
    def build_tree(self,array):
        #set the bottom of the tree to our array
        for i in range(self.n):
            self.max_tree[self.n + i] = array[i]
        
        #set the first half of the tree which is our calculations/internal
        #children are i * 2 and i*2 + 1 and parent is i // 2
        for i in range(self.n-1,0,-1):
            self.max_tree[i] = max(self.max_tree[i << 1], self.max_tree[(i << 1)+1])
    
    def update(self,p,value):
        self.max_tree[p+self.n] = value
        p += self.n
        #go up each parent until we hit the root
        while p > 1:
            p = p >> 1
            #go back up the tree and recalculate max
            self.max_tree[p] = max(self.max_tree[p << 1], self.max_tree[(p << 1) ^ 1])
    def query_max(self,l,r):
        l += self.n
        r += self.n
        
        max_val = float('-inf')
        while l < r:
            if l & 1:
                max_val = max(max_val, self.max_tree[l])
                l += 1
            if r & 1:
                r -= 1
                max_val = max(max_val, self.max_tree[r])
            
            #go to parent
            l = l >> 1
            r = r >> 1
        
        return max_val
            
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        dp = [0] * (max(nums) + 1)
    
        seg = SegmentTree(dp)
        mx = 1
        for num in nums:
            tmx = 1
            if num - 1 >= 1:
                tmx = seg.query_max(max(0,num - k), num) + 1
            
            mx = max(mx, tmx)
            seg.update(num,tmx)
            
        return mx
            
                    
                    
                    