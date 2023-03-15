# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        
        q = deque()
        q.append((root,0))
        
        level = 0
        gap = 0
        while q:
            
            nodes = 2 ** level
            num = 0
            last = -1
            if gap:
                return False
            for i in range(len(q)):
                
                node,val = q.popleft()
                nodes -=1
                if abs(val - last) > 1:
                    return False
                last = val
                if node.left:
                    q.append((node.left,num))
                num +=1
                if node.right:
                    q.append((node.right, num))
                num +=1
                if node.right and not node.left:
                    return False
                
            
            if nodes > 0:
                gap += 1
            level +=1

        return True
                
                
                