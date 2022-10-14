# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if head.next is None:
            return None

        slow,fast = head,head
        prev = slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        
        prev.next = prev.next.next
        
        return head
        