# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dhead = ListNode(-1)
        dhead.next = head
        t = dhead
        
        while dhead and dhead.next:
            thead = dhead
            while thead and thead.next and thead.next.val == val:
                thead = thead.next
            
            
            dhead.next = thead.next
            dhead = dhead.next
        
        
        return t.next
                