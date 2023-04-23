# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode()
        dnode = node
        head = head.next   
        running = 0
        while head:
        
            if head.val == 0:
                node.next = ListNode(running)
                node = node.next
                running = 0
            
            else:
                running += head.val
            
            head = head.next
        
        
        return dnode.next
            