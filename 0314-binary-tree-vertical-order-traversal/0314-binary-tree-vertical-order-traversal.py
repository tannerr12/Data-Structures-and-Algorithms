# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        res = defaultdict(list)
        def dfs(root,row):
            
            if root is None:
                return root
            
            res[row].append(root.val)
            dfs(root.left, row -1)
            dfs(root.right, row +1)
            
            
        
        dfs(root,0)
        #print(res)
        ans = []
        
        for i in range(-100, 101):
            if i in res:
                ans.append(res[i])
        
        return ans
        """
        if root is None:
            return []
        q = deque()
        q.append((root,0))
        res = defaultdict(list)
        while q:
            
            for i in range(len(q)):
                node, col = q.popleft()
                
                res[col].append(node.val)
                
                if node.left:
                    q.append((node.left, col -1))
                if node.right:
                    q.append((node.right, col + 1))
        
        
     
        ans = []
        
        for i in range(-100, 101):
            if i in res:
                ans.append(res[i])
        
        return ans
                