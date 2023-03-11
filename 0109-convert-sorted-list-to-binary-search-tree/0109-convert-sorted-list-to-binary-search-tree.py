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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:


        def fastSlow(head):

            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            

            if prev:
                prev.next = None
            return slow
        

        def divide(head):

            if not head:
                return None

            m = fastSlow(head)

            root = TreeNode(m.val)

            if m == head:
                return root

            root.left = divide(head)

            root.right = divide(m.next)

            return root
        

        return divide(head)
