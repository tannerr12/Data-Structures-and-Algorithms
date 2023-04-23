# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        dnode = head
        prev = None
        head = head.next   
        
        while head:
        
            if head.val == 0:
                prev = node
                node = node.next
                node.val = 0
            else:
                node.val += head.val
            
            head = head.next
        
        if prev:
            prev.next = None
        return dnode
            