class Node:
    
    def __init__(self,val,cnt):
        
        self.val = val
        self.left = None
        self.right = None
        self.cnt = cnt

class KthLargest:
    
    def dfs(self,root,val):
        
        if root == None:
            return Node(val,1)
        
        if root.val >= val:
            root.left = self.dfs(root.left,val)
        elif root.val < val:
            root.right = self.dfs(root.right,val)
        
        root.cnt +=1
        return root
    
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        for i in range(len(nums)):
            self.root = self.dfs(self.root,nums[i])
        self.mk = k

    def search(self,root, k):
 
        m =0
        if root.right:
            m = root.right.cnt
    
        if m+1 == k:
            return root.val
        if m < k:
            return self.search(root.left,k - m - 1)
        else:
            return self.search(root.right,k)
        
    
            
        
    def add(self, val: int) -> int:
        self.root = self.dfs(self.root,val)
        #find kth largest
        res = self.search(self.root,self.mk)
        return res

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)