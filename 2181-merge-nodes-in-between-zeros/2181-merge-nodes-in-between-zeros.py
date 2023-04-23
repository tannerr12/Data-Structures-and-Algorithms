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
        running = 0
        while head:
        
            if head.val == 0:
                prev = node
                node.val = running
                node = node.next
                running = 0
            
            else:
                running += head.val
            
            head = head.next
        
        if prev:
            prev.next = None
        return dnode
            