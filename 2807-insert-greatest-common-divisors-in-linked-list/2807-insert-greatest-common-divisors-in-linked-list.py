# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        h = head
        prev = head
        
        while head.next:
            
            head = head.next
            prev.next = ListNode(gcd(prev.val, head.val))
            prev.next.next = head
            prev = head
            
        
        
        return h
            