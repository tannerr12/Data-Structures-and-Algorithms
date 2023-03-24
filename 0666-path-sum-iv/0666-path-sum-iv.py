class Node:
    
    def __init__(self,val):
        
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        
        l = nums[0] // 100
        p = (nums[0] // 10) % 10
        v = nums[0] % 10
        
        root = Node(v)
        
        q = deque()
        q.append((root, p, l))
        idx = 1
        level = 1
        while q and idx < len(nums):
            
            calc = 2 ** (level -1)
            num = 1
            for i in range(len(q)):
                
                node,p,l = q.popleft()
                
                lev = nums[idx] // 100
                pos = (nums[idx] // 10) % 10
                val = nums[idx] % 10
                
                if lev == l + 1 and pos == (p*2)-1:
                    node.left = Node(val)
                    idx +=1
                    q.append((node.left, pos,lev))
                
                if idx >= len(nums):
                    break
                lev = nums[idx] // 100
                pos = (nums[idx] // 10) % 10
                val = nums[idx] % 10
                
                
                if lev == l + 1 and pos == (p*2):
                    node.right = Node(val)
                    idx +=1
                    q.append((node.right, pos,lev))
                
                if idx >= len(nums):
                    break
                
                
    
                
                
        def dfs(root):
            
            if root is None:
                return [0, 0]
            
            res = 0
            l,r = 0,0
            v1,v2= 0,0
            if root.left:
                v1,l = dfs(root.left)
            
            if root.right:
                v2,r = dfs(root.right) 
            
            if not root.left and not root.right:
                return [root.val,1]
            res = v1 + v2
            val = root.val * (l + r)
            return [res + val, l + r]
        
        return dfs(root)[0]
        
        