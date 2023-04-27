# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        headCopy = head
        @cache
        def dfs(root,head,started):
            nonlocal headCopy
            if head is None:
                return True
            if root is None:
                return False
            
            prev = head
            res = False
            if root.val == head.val:
                head = head.next
            elif started:
                head = headCopy
            
            if root.val == headCopy.val:
                res = res or dfs(root.left,headCopy.next, True)
                res = res or dfs(root.right, headCopy.next, True)
                
            res = res or dfs(root.left,head,head != headCopy)
            res = res or dfs(root.right,head,head != headCopy)
             
           
            return res
        
        
        return dfs(root,head,False)
        
        